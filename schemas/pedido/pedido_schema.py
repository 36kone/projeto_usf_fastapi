from datetime import datetime, date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PedidoSchema(BaseModel):
    id: int
    cliente_id: int
    data: date
    status: str
    total: float
    produto_id: int
    


class CriarPedido(BaseModel):
    cliente_id: int
    data: date
    status: str
    total: float
    produto_id: int

class AtualizarPedido(BaseModel):
    id: int
    cliente_id: Optional[int] = None
    data: Optional[date] = None
    status: Optional[str] = None
    total: Optional[float] = None
    produto_id: Optional[int] = None



class PedidoResposta(PedidoSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
