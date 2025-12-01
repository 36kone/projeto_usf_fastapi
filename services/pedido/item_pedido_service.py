from sqlalchemy.orm import Session
from sqlalchemy import delete

from schemas.pedido.item_pedido_schema import CriarItemPedido
from models.pedido.item_pedido import ItemPedido


def criar_item_pedido(item_pedido: CriarItemPedido, session: Session):
    entity = ItemPedido(**item_pedido.model_dump(exclude_unset=True))

    session.add(entity)
    return entity


def recriar_item_pedido(pedido_id: int, itens: list[CriarItemPedido], session: Session):
    session.execute(delete(ItemPedido).where(ItemPedido.pedido_id == pedido_id))

    new_entities = [
        ItemPedido(**item.model_dump(exclude_unset=True), pedido_id=pedido_id)
        for item in itens
    ]

    session.add_all(new_entities)
    return new_entities
