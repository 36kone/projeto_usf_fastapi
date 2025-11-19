from sqlalchemy.orm import Session
from schemas.pedido.pedido_schema import CriarPedido, AtualizarPedido
from models.pedido.pedido import Pedido
from datetime import datetime,UTC
from fastapi import HTTPException

def criar_pedido(pedido: CriarPedido, session: Session):
    entity = Pedido(**pedido.model_dump(exclude_unset=True))

    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity

def ler_pedidos(session: Session):
    return session.query(Pedido).limit(10).all()

def pegar_pedido_por_id(id: int, session: Session):
    entity =  session.query(Pedido).filter(Pedido.id == id).first()
    
    if not entity:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    return entity

def atualizar_pedido(dados: AtualizarPedido, session: Session):
    entity = pegar_pedido_por_id(dados.id, session)
    
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
    entity = pegar_pedido_por_id(id, session)
    
    entity.deleted_at = datetime.now(UTC)
    
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return {"message": "Pedido deletado."}


def hard_delete_pedido(id: int, session: Session):
    entity = pegar_pedido_por_id(id, session)
    
    session.delete(entity)
    session.commit()
    return {"message": "Pedido deletado permanentemante."}


    