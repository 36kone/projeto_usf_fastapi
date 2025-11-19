from sqlalchemy.orm import Session

from core.security import get_password_hash
from datetime import datetime,UTC
from fastapi import HTTPException
from schemas.pedido.pedido_schema import CriarPedido, AtualizarPedido
from models.pedido.pedido import Pedido


def criar_pedido(pedido: CriarPedido,session: Session):
    entity = Pedido(**pedido.model_dump(exclude_unset=True))
    
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity

def ler_pedidos(session: Session):
    ## SELECT * FROM produto;

    return session.query(Pedido).limit(10).all()

def pegar_pedido(id: int, session: Session):
    entity =  session.query(Pedido).filter(Pedido.id == id).first()
    
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


def hard_delete_pedido (id: int, session: Session):
    entity = pegar_pedido(id, session)
    
    session.delete(entity)
    session.commit()
    return {"message": "Pedido deletado permanentemante."}


    