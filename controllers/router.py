from fastapi import APIRouter

from controllers.clientes.clientes_controller import clientes_router
from controllers.pedidos.pedidos_controller import pedidos_router
from controllers.produtos.produtos_controller import produtos_router
from controllers.login.login_controller import login_router

api_router = APIRouter()

api_router.include_router(login_router, prefix="/login", tags=["Login"])
api_router.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(pedidos_router, prefix="/pedidos", tags=["Pedidos"])
api_router.include_router(produtos_router, prefix="/produtos", tags=["Produtos"])
