from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import pegar_sessao
from services.login import login_service
from schemas.auth.auth_schema import Token

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
