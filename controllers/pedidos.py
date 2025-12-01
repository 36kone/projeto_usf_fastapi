from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.pedido.pedido_schema import CriarPedido, PedidoResposta, AtualizarPedido
from db.database import pegar_sessao
from services.pedido import pedido_service

pedidos_router = APIRouter()


@pedidos_router.post(
    "/",
    response_model=PedidoResposta,
    summary="Cria um novo pedido.",
    description="Não passar 'pedido_id'; ele é gerado automaticamente. Cada item deve conter 'produto_id' e 'quantidade'.",
)
def criar_pedido(pedido: CriarPedido, session: Session = Depends(pegar_sessao)):
    return pedido_service.criar_pedido(pedido, session)


@pedidos_router.get(
    "/",
    response_model=list[PedidoResposta],
    summary="Lista todos os pedidos cadastrados.",
    description="Retorna todos os pedidos, incluindo os itens de cada pedido.",
)
def ler_pedidos(session: Session = Depends(pegar_sessao)):
    return pedido_service.ler_pedidos(session)


@pedidos_router.get(
    "/{id}",
    response_model=PedidoResposta,
    summary="Busca um pedido pelo ID.",
    description="Retorna os dados do pedido especificado, incluindo os itens.",
)
def pegar_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.pegar_pedido_por_id(id, session)


@pedidos_router.put(
    "/{id}",
    response_model=PedidoResposta,
    summary="Atualiza os dados de um pedido existente.",
    description="Campos opcionais: cliente_id, data, status, total, itens. O ID do pedido deve ser informado.",
)
def atualizar_pedido(dados: AtualizarPedido, session: Session = Depends(pegar_sessao)):
    return pedido_service.atualizar_pedido(dados, session)


@pedidos_router.delete(
    "/{id}",
    summary="Soft delete de pedido.",
    description="Marca o pedido como deletado sem remover do banco.",
)
def soft_delete_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.soft_delete_pedido(id, session)


@pedidos_router.delete(
    "/hard-delete/{id}",
    summary="Hard delete de pedido.",
    description="Remove permanentemente o pedido do banco de dados.",
)
def hard_delete_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.hard_delete_pedido(id, session)
