from database import SessionLocal
from models import Cliente, Produto, Pedido, ItemPedido

def limpar_banco():
    session = SessionLocal()
    session.query(ItemPedido).delete()
    session.query(Pedido).delete()
    session.query(Produto).delete()
    session.query(Cliente).delete()
    session.commit()
    session.close()

if __name__ == "__main__":
    limpar_banco()
    print("Banco de dados limpo com sucesso.")