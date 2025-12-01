from sqlalchemy.orm import Session
from sqlalchemy import select

from datetime import datetime, UTC
from fastapi import HTTPException
from schemas.pedido.pedido_schema import CriarPedido, AtualizarPedido
from models import Pedido, Produto
from services.pedido.item_pedido_service import criar_item_pedido, recriar_item_pedido


def criar_pedido(pedido: CriarPedido, session: Session):
    entity = Pedido(**pedido.model_dump(exclude_unset=True, exclude={"itens"}))

    entity.total = 0.0

    session.add(entity)
    session.flush()

    total = 0.0
    for item in pedido.itens:
        item.pedido_id = entity.id
        produto_preco = session.scalar(
            select(Produto.preco).where(Produto.id == item.produto_id)
        )
        total += produto_preco * item.quantidade
        criar_item_pedido(item, session)

    entity.total = total
    session.commit()
    return entity


def ler_pedidos(session: Session):
    ## SELECT * FROM produto;

    return session.query(Pedido).limit(10).all()


def pegar_pedido(id: int, session: Session):
    entity = session.query(Pedido).filter(Pedido.id == id).first()

    if not entity:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    return entity


def atualizar_pedido(dados: AtualizarPedido, session: Session):
    entity = pegar_pedido(dados.id, session)

    if not entity:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    try:
        for key, value in dados.model_dump(exclude_unset=True).items():
            setattr(entity, key, value)

        recriar_item_pedido(entity.id, dados.itens, session)

        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    except Exception as e:
        session.rollback()
        raise e


def soft_delete_pedido(id: int, session: Session):
    entity = pegar_pedido(id, session)

    entity.deleted_at = datetime.now(UTC)

    session.add(entity)
    session.commit()
    session.refresh(entity)
    return {"message": "Produto deletado."}


def hard_delete_pedido(id: int, session: Session):
    entity = pegar_pedido(id, session)

    session.delete(entity)
    session.commit()
    return {"message": "Pedido deletado permanentemante."}
