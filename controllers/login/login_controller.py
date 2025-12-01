from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import pegar_sessao
from core.authentication import pegar_usuario_logado
from services.login import login_service
from schemas.auth.auth_schema import Token
from schemas.cliente.cliente_schema import ClienteResposta
from models import Cliente
from services.cliente.cliente_service import pegar_cliente_por_id

login_router = APIRouter()


@login_router.post(
    "/",
    response_model=Token,
    summary="Realiza login do cliente",
    description="Autentica um cliente usando email e senha e retorna um token JWT de acesso.",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(pegar_sessao),
):
    return login_service.login(form_data, session)


@login_router.get(
    "/me",
    response_model=ClienteResposta,
    summary="Retorna os dados do usuário autenticado",
    description="Retorna os dados do usuário autenticado.",
)
def ler_usuario_autenticado(
    usuario: Cliente = Depends(pegar_usuario_logado),
    session: Session = Depends(pegar_sessao),
):
    return pegar_cliente_por_id(usuario.id, session)
