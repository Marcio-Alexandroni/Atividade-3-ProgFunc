from database import engine, SessionLocal, Base
from models import Cliente, Produto

def main():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    # só insere se não houver dados
    if not session.query(Cliente).first():
        session.add_all([
            Cliente(nome="Alice",  saldo=500.0),
            Cliente(nome="Bob",    saldo=300.0),
            Cliente(nome="Clara",  saldo=800.0),
        ])
    if not session.query(Produto).first():
        session.add_all([
            Produto(nome="Caneta",  preco=2.50, estoque=100),
            Produto(nome="Caderno", preco=15.0, estoque=50),
            Produto(nome="Mochila", preco=120.0, estoque=10),
        ])
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
