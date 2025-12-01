from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import Depends, HTTPException, Security
from fastapi.security import (
    OAuth2PasswordBearer,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from jose import jwt, JWTError
from sqlalchemy import select

from core.config import settings
from models.cliente.cliente import Cliente
from schemas.auth.auth_schema import Token
from schemas.cliente.cliente_schema import ClienteResposta
from db.database import pegar_sessao

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")
bearer_scheme = HTTPBearer(auto_error=False)


def criar_token_de_acesso(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Cria um token JWT de acesso.
    """
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def criar_token_do_cliente(user: Cliente) -> Token:
    """
    Cria um token JWT para o cliente e retorna o Token schema.
    """
    access_token = criar_token_de_acesso({"sub": str(user.id), "username": user.email})
    return Token(
        access_token=access_token,
        token_type="bearer",
        user=ClienteResposta.model_validate(user),
    )


def decode_access_token(token: str) -> dict[str, Any] | None:
    """
    Decodifica o token JWT e retorna o payload.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None


def verificar_token(token: str = Depends(oauth2_scheme)) -> str:
    """
    Verifica se o token JWT é válido e retorna o ID do usuário.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Acesso negado, verifique seu token"
        )

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Acesso negado, verifique o tempo de expiração do token",
        )
    return user_id


def pegar_usuario_logado(
    bearer: HTTPAuthorizationCredentials = Security(bearer_scheme),
    session=Depends(pegar_sessao),
    oauth2: str | None = Depends(oauth2_scheme),
) -> Cliente:
    """
    Retorna o usuário logado a partir do token Bearer ou OAuth2.
    """
    token = bearer.credentials if bearer else oauth2
    if not token:
        raise HTTPException(status_code=401, detail="Não autenticado")

    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        user_id = payload.get("sub")
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )

    query = select(Cliente).where(Cliente.id == user_id)
    user = session.scalar(query)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
