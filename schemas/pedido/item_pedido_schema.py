from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ItemPedidoSchema(BaseModel):
    id: int
    pedido_id: int
    produto_id: int
    quantidade: int


class CriarItemPedido(BaseModel):
    pedido_id: Optional[int] = None
    produto_id: int
    quantidade: int


class ItemPedidoResposta(ItemPedidoSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
