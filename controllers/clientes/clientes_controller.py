from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.cliente.cliente_schema import (
    CriarCliente,
    ClienteResposta,
    AtualizarCliente,
)
from db.database import pegar_sessao
from services.cliente import cliente_service

clientes_router = APIRouter()


@clientes_router.post(
    "/",
    response_model=ClienteResposta,
    summary="Cria um novo cliente com os dados fornecidos.",
    description="Campos obrigatórios: nome, email, celular, senha, endereco.",
)
def criar_cliente(cliente: CriarCliente, session: Session = Depends(pegar_sessao)):
    return cliente_service.criar_cliente(cliente, session)


@clientes_router.get(
    "/",
    response_model=list[ClienteResposta],
    summary="Lista todos os clientes cadastrados.",
    description="Retorna todos os clientes, incluindo os que não foram deletados.",
)
def ler_cliente(session: Session = Depends(pegar_sessao)):
    return cliente_service.ler_cliente(session)


@clientes_router.get(
    "/{id}",
    response_model=ClienteResposta,
    summary="Busca um cliente pelo ID.",
    description="Retorna os dados do cliente especificado pelo ID.",
)
def pegar_cliente(id: int, session: Session = Depends(pegar_sessao)):
    return cliente_service.pegar_cliente_por_id(id, session)


@clientes_router.put(
    "/{id}",
    response_model=ClienteResposta,
    summary="Atualiza os dados de um cliente existente.",
    description="Campos opcionais: nome, email, celular, endereco. O ID do cliente deve ser informado.",
)
def atualizar_cliente(
    dados: AtualizarCliente, session: Session = Depends(pegar_sessao)
):
    return cliente_service.atualizar_cliente(dados, session)


@clientes_router.delete(
    "/{id}",
    summary="Soft delete de cliente.",
    description="Marca o cliente como deletado sem remover do banco.",
)
def soft_delete_cliente(id: int, session: Session = Depends(pegar_sessao)):
    return cliente_service.soft_delete_cliente(id, session)


@clientes_router.delete(
    "/hard-delete/{id}",
    summary="Hard delete de cliente.",
    description="Remove permanentemente o cliente do banco de dados.",
)
def hard_delete_cliente(id: int, session: Session = Depends(pegar_sessao)):
    return cliente_service.hard_delete_cliente(id, session)
