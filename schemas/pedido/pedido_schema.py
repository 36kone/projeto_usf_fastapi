from datetime import datetime, date
from typing import Optional, List

from pydantic import BaseModel, ConfigDict
from schemas.pedido.item_pedido_schema import CriarItemPedido


class PedidoSchema(BaseModel):
    id: int
    cliente_id: int
    data: date
    status: str
    total: float


class CriarPedido(BaseModel):
    cliente_id: int
    data: date
    itens: list[CriarItemPedido]


class AtualizarPedido(BaseModel):
    id: int
    cliente_id: Optional[int] = None
    data: Optional[date] = None
    status: Optional[str] = None
    total: Optional[float] = None
    itens: Optional[List[CriarItemPedido]] = None


class PedidoResposta(PedidoSchema):
    id: int
    itens: list[CriarItemPedido]
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
