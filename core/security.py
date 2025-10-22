from datetime import datetime, timezone, timedelta

from core.config import settings
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from db.database import pegar_sessao
from main import oauth2_scheme


def criar_token(id_usuario, duracao_token=timedelta(minutes=30)):
    data_expire = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub": str(id_usuario), "exp": data_expire}
    jwt_codificado = jwt.encode(dic_info, settings.SECRET_KEY, settings.ALGORITHM)
    return jwt_codificado


def verificar_token(
    token: str = Depends(oauth2_scheme), session: Session = Depends(pegar_sessao)
):
    try:
        dic_info = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        id_usuario = dic_info.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso negado, verifique o token")
    # usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if not id_usuario:
        raise HTTPException(
            status_code=401, detail="Acesso invalido, verifique a validade do token"
        )
    return  # usuario
