from database import engine, SessionLocal, Base
from models import Cliente, Produto, Pedido, ItemPedido

def main():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    # só insere se não houver dados
    if not session.query(Cliente).first():
        session.add_all([
            Cliente(nome="Paulo",  saldo=500.0),
            Cliente(nome="Cesar",    saldo=300.0),
            Cliente(nome="Marcio",  saldo=800.0),
        ])
    if not session.query(Produto).first():
        session.add_all([
            Produto(nome="Caneta",  preco=2.50, estoque=100),
            Produto(nome="Caderno", preco=15.0, estoque=50),
            Produto(nome="Mochila", preco=120.0, estoque=10),
        ])
    session.commit()
    session.close()

def limpar_banco():
    session = SessionLocal()
    session.query(ItemPedido).delete()
    session.query(Pedido).delete()
    session.query(Produto).delete()
    session.query(Cliente).delete()
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
    # limpar_banco()
    # print("Banco de dados limpo.")
