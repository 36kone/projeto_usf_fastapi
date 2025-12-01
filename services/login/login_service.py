from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.security import verify_password
from core.authentication import criar_token_do_cliente
from services.cliente.cliente_service import pegar_cliente_por_email

<<<<<<< HEAD
=======

>>>>>>> 281ff50 (feat: criado login para clientes)
def login(form_data: OAuth2PasswordRequestForm, session: Session):
    cliente = pegar_cliente_por_email(form_data.username, session)

    if not verify_password(form_data.password, str(cliente.senha)):
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    return criar_token_do_cliente(cliente)
