from sqlalchemy import Column, String, TIMESTAMP, func, Integer, Float

from db.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)