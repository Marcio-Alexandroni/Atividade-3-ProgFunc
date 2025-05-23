from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id    = Column(Integer, primary_key=True, index=True)
    nome  = Column(String(100), nullable=False)
    saldo = Column(Float, nullable=False)
    pedidos = relationship("Pedido", back_populates="cliente")

class Produto(Base):
    __tablename__ = "produtos"
    id       = Column(Integer, primary_key=True, index=True)
    nome     = Column(String(100), nullable=False)
    preco    = Column(Float, nullable=False)
    estoque  = Column(Integer, nullable=False)
    itens    = relationship("ItemPedido", back_populates="produto")

class Pedido(Base):
    __tablename__ = "pedidos"
    id         = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    data       = Column(DateTime(timezone=True), server_default=func.now())
    cliente    = relationship("Cliente", back_populates="pedidos")
    itens      = relationship("ItemPedido", back_populates="pedido")

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id            = Column(Integer, primary_key=True, index=True)
    pedido_id     = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id    = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade    = Column(Integer, nullable=False)
    preco_unit    = Column(Float, nullable=False)
    pedido        = relationship("Pedido", back_populates="itens")
    produto       = relationship("Produto", back_populates="itens")
