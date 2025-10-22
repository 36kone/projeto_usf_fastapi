from fastapi import APIRouter

from controllers.clientes import clientes_router
from controllers.login import login_router
from controllers.pedidos import pedidos_router
from controllers.produtos import produtos_router

api_router = APIRouter()

api_router.include_router(login_router, prefix="/auth", tags=["Auth"])
api_router.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(pedidos_router, prefix="/pedidos", tags=["Pedidos"])
api_router.include_router(produtos_router, prefix="/produtos", tags=["Produtos"])
