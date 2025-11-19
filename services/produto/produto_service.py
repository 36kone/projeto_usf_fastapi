from sqlalchemy.orm import Session

from core.security import get_password_hash
from datetime import datetime,UTC
from fastapi import HTTPException
from schemas.produto.produto_schema import CriarProduto, AtualizarProduto
from models.produto.produto import Produto


def criar_produto(produto: CriarProduto,session: Session):
    entity = Produto(**produto.model_dump(exclude_unset=True))
    
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity

def ler_produtos(session: Session):
    ## SELECT * FROM produto;

    return session.query(Produto).limit(10).all()

def pegar_produto(id: int, session: Session):
    entity =  session.query(Produto).filter(Produto.id == id).first()
    
    if not entity:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return entity


def atualizar_produto(dados: AtualizarProduto, session: Session):
    entity = pegar_produto(dados.id, session)
    
    if not entity:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    
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


def soft_delete_produto(id: int, session: Session):
    entity = pegar_produto(id, session)
    
    entity.deleted_at = datetime.now(UTC)
    
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return {"message": "Produto deletado."}


def hard_delete_produto (id: int, session: Session):
    entity = pegar_produto(id, session)
    
    session.delete(entity)
    session.commit()
    return {"message": "Produto deletado permanentemante."}


    