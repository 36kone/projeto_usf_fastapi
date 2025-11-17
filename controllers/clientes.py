from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.Cliente.cliente_schema import CriarCliente, ClienteResposta, AtualizarCliente
from db.database import pegar_sessao
from services.cliente import cliente_service

clientes_router = APIRouter()


@clientes_router.post("/", response_model = ClienteResposta)
def criar_cliente(cliente: CriarCliente, session: Session = Depends(pegar_sessao)):
    return cliente_service.criar_cliente(cliente, session)


@clientes_router.get("/", response_model=list[ClienteResposta])
def ler_cliente(session: Session = Depends(pegar_sessao)):
    return cliente_service.ler_cliente(session)


@clientes_router.get("/{id}", response_model=ClienteResposta)
def pegar_cliente(id: int ,session: Session = Depends(pegar_sessao)):
    return cliente_service.pegar_cliente(id,session)


@clientes_router.put("/{id}", response_model=ClienteResposta)
def atualizar_cliente(dados: AtualizarCliente,session: Session = Depends(pegar_sessao)):
    return cliente_service.atualizar_cliente(dados, session)


@clientes_router.delete("/{id}")
def soft_delete_cliente(id: int,session: Session = Depends(pegar_sessao)):
    return cliente_service.soft_delete_cliente(id ,session)

@clientes_router.delete("/hard-delete/{id}")
def hard_delete_cliente(id: int, session: Session = Depends(pegar_sessao)):
    return cliente_service.hard_delete_cliente(id ,session)

