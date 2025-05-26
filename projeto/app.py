from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
from database import SessionLocal
from models import Cliente, Produto, Pedido, ItemPedido
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=4)

def processar_pedido():
    try:
        # abre sessão completa
        session = SessionLocal()
        try:
            # escolhe cliente e produto
            cliente = session.query(Cliente).order_by(func.rand()).first()
            produto = session.query(Produto).order_by(func.rand()).first()
            # validações
            if cliente.saldo < produto.preco or produto.estoque < 1:
                logging.warning(f"Pedido falhou: Cliente {cliente.nome} (Saldo: {cliente.saldo}), Produto {produto.nome} (Estoque: {produto.estoque})")
                return
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
            session.commit()
            logging.info(f"Pedido criado: Cliente {cliente.nome}, Produto {produto.nome}, Pedido ID {pedido.id}")
        except Exception as e:
            session.rollback()
            logging.error(f"Erro ao processar pedido: {e}")
        finally:
            session.close()
    except Exception as e:
        logging.error(f"Erro ao inicializar sessão: {e}")

@app.route("/pedido", methods=["POST"])
def novo_pedido():
    try:
        executor.submit(processar_pedido)
        return jsonify({"status": "em processamento"}), 202
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except SQLAlchemyError as e:
        return jsonify({"erro": "Erro no banco de dados"}), 500

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

@app.route("/status", methods=["GET"])
def status():
    # Retorna o número de pedidos em andamento e concluídos
    session = SessionLocal()
    total_pedidos = session.query(Pedido).count()
    session.close()
    return jsonify({"pedidos_concluidos": total_pedidos})

if __name__ == "__main__":
    app.run(debug=True)
