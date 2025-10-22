from fastapi import APIRouter

produtos_router = APIRouter()


@produtos_router.get("/")
async def produtos():
    return {"produtos teste"}
