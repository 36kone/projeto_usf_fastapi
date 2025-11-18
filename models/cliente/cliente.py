from sqlalchemy import Column, String, TIMESTAMP, func, Integer

from db.database import Base


class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    celular = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)