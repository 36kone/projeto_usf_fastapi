from sqlalchemy.orm import Session
from schemas.cliente.cliente_schema import CriarCliente, AtualizarCliente
from models.cliente.cliente import Cliente
from core.security import get_password_hash
from datetime import datetime,UTC
from fastapi import HTTPException

def criar_cliente(cliente: CriarCliente,session: Session):
    entity = Cliente(
        nome=cliente.nome, 
        email=cliente.email,
        celular=cliente.celular,
        endereco=cliente.endereco,
        senha = get_password_hash(cliente.senha)
    )

    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity

def ler_cliente(session: Session):
    ## SELECT * FROM clientes;

    return session.query(Cliente).limit(10).all()

def pegar_cliente(id: int, session: Session):
    entity =  session.query(Cliente).filter(Cliente.id == id).first()
    
    if not entity:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

def atualizar_cliente(dados: AtualizarCliente, session: Session):
    entity = pegar_cliente(dados.id, session)
    
    if not entity:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
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


def soft_delete_cliente(id: int, session: Session):
    entity = pegar_cliente(id, session)
    
    entity.deleted_at = datetime.now(UTC)
    
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return {"message": "Cliente deletado."}


def hard_delete_cliente (id: int, session: Session):
    entity = pegar_cliente(id, session)
    
    session.delete(entity)
    session.commit()
    return {"message": "Cliente deletado permanentemante."}


    