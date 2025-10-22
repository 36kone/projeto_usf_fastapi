from fastapi import APIRouter

pedidos_router = APIRouter()


@pedidos_router.get("/")
async def pedidos():
    return {"pedidos teste"}
