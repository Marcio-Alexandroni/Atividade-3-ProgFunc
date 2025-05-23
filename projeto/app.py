from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
from database import SessionLocal
from models import Cliente, Produto, Pedido, ItemPedido
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=4)

def processar_pedido():
    # abre transação explícita
    with SessionLocal().begin() as session:
        # escolhe cliente e produto
        cliente = session.query(Cliente).order_by(func.rand()).first()
        produto = session.query(Produto).order_by(func.rand()).first()
        # validações
        if cliente.saldo < produto.preco or produto.estoque < 1:
            raise ValueError("Saldo insuficiente ou estoque zerado")
        # cria pedido e item
        pedido = Pedido(cliente_id=cliente.id)
        session.add(pedido)
        session.flush()
        item = ItemPedido(
            pedido_id=pedido.id,
            produto_id=produto.id,
            quantidade=1,
            preco_unit=produto.preco
        )
        session.add(item)
        # atualiza saldo/estoque
        cliente.saldo  -= produto.preco
        produto.estoque -= 1
    # ao sair do with, faz commit automático; em caso de erro, rollback

@app.route("/pedido", methods=["POST"])
def novo_pedido():
    executor.submit(processar_pedido)
    return jsonify({"status": "em processamento"}), 202

@app.route("/relatorio", methods=["GET"])
def relatorio():
    session = SessionLocal()
    pedidos = session.query(Pedido).all()
    resp = []
    for p in pedidos:
        resp.append({
            "id": p.id,
            "cliente": p.cliente.nome,
            "data": p.data.isoformat(),
            "itens": [
                {"produto": i.produto.nome, "qtde": i.quantidade, "preco": i.preco_unit}
                for i in p.itens
            ]
        })
    session.close()
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)
