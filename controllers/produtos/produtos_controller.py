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


@produtos_router.post(
    "/",
    response_model=ProdutoResposta,
    summary="Cria um novo produto com os dados fornecidos.",
    description="Campos obrigatórios: nome, descricao, preco, estoque.",
)
def criar_produto(produto: CriarProduto, session: Session = Depends(pegar_sessao)):
    return produto_service.criar_produto(produto, session)


@produtos_router.get(
    "/",
    response_model=list[ProdutoResposta],
    summary="Lista todos os produtos cadastrados.",
    description="Retorna todos os produtos, incluindo os que não foram deletados.",
)
def ler_produtos(session: Session = Depends(pegar_sessao)):
    return produto_service.ler_produtos(session)


@produtos_router.get(
    "/{id}",
    response_model=ProdutoResposta,
    summary="Busca um produto pelo ID.",
    description="Retorna os dados do produto especificado pelo ID.",
)
def pegar_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.pegar_produto_por_id(id, session)


@produtos_router.put(
    "/{id}",
    response_model=ProdutoResposta,
    summary="Atualiza os dados de um produto existente.",
    description="Campos opcionais: nome, descricao, preco, estoque. O ID do produto deve ser informado.",
)
def atualizar_produto(
    dados: AtualizarProduto, session: Session = Depends(pegar_sessao)
):
    return produto_service.atualizar_produto(dados, session)


@produtos_router.delete(
    "/{id}",
    summary="Soft delete de produto.",
    description="Marca o produto como deletado sem remover do banco.",
)
def soft_delete_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.soft_delete_produto(id, session)


@produtos_router.delete(
    "/hard-delete/{id}",
    summary="Hard delete de produto.",
    description="Remove permanentemente o produto do banco de dados.",
)
def hard_delete_produto(id: int, session: Session = Depends(pegar_sessao)):
    return produto_service.hard_delete_produto(id, session)
