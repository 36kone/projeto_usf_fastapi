from sqlalchemy import Column, TIMESTAMP, func, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class ItemPedido(Base):
    __tablename__ = "item_pedidos"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False, default=1)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    pedido = relationship("Pedido", back_populates="itens")
