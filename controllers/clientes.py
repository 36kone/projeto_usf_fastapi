from fastapi import APIRouter

clientes_router = APIRouter()


@clientes_router.get("/")
async def clientes():
    return {"clientes teste"}
