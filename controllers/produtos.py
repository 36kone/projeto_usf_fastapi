from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.produto.produto_schema import (
    CriarProduto,
    ProdutoResposta,
    AtualizarProduto,
)
from db.database import pegar_sessao
from services.produto import produto_service

produtos_router = APIRouter()


@produtos_router.post("/", response_model=ProdutoResposta)
def criar_produto(produto: CriarProduto, session: Session = Depends(pegar_sessao)):
    return produto_service.criar_produto(produto, session)


@produtos_router.get("/", response_model=list[ProdutoResposta])
def ler_produtos(session: Session = Depends(pegar_sessao)):
    return produto_service.ler_produtos(session)


@produtos_router.get("/{id}", response_model=ProdutoResposta)
def pegar_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.pegar_produto(id, session)


@produtos_router.put("/{id}", response_model=ProdutoResposta)
def atualizar_produto(
    dados: AtualizarProduto, session: Session = Depends(pegar_sessao)
):
    return produto_service.atualizar_produto(dados, session)


@produtos_router.delete("/{id}")
def soft_delete_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.soft_delete_produto(id, session)


@produtos_router.delete("/hard-delete/{id}")
def hard_delete_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.hard_delete_produto(id, session)
