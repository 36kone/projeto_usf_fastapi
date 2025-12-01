from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.pedido.pedido_schema import CriarPedido, PedidoResposta, AtualizarPedido
from db.database import pegar_sessao
from services.pedido import pedido_service

pedidos_router = APIRouter()


@pedidos_router.post("/", response_model=PedidoResposta)
def criar_pedido(pedido: CriarPedido, session: Session = Depends(pegar_sessao)):
    return pedido_service.criar_pedido(pedido, session)


@pedidos_router.get("/", response_model=list[PedidoResposta])
def ler_pedidos(session: Session = Depends(pegar_sessao)):
    return pedido_service.ler_pedidos(session)


@pedidos_router.get("/{id}", response_model=PedidoResposta)
def pegar_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.pegar_pedido(id, session)


@pedidos_router.put("/{id}", response_model=PedidoResposta)
def atualizar_pedido(dados: AtualizarPedido, session: Session = Depends(pegar_sessao)):
    return pedido_service.atualizar_pedido(dados, session)


@pedidos_router.delete("/{id}")
def soft_delete_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.soft_delete_pedido(id, session)


@pedidos_router.delete("/hard-delete/{id}")
def hard_delete_pedido(id: int, session: Session = Depends(pegar_sessao)):
    return pedido_service.hard_delete_pedido(id, session)
