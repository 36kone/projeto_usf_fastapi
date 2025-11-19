from sqlalchemy import Column, String, TIMESTAMP, func, Integer, Float, Date, ForeignKey

from db.database import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    data = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    total = Column(Float, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)