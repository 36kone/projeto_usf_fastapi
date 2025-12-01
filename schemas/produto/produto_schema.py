from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProdutoSchema(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    estoque: int


class CriarProduto(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int


class AtualizarProduto(BaseModel):
    id: int
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    estoque: Optional[int] = None


class ProdutoResposta(ProdutoSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
