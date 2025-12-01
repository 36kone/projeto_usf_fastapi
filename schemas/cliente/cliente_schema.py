from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class ClienteSchema(BaseModel):
    id: int
    nome: str
    email: EmailStr
    celular: str
    endereco: str


class CriarCliente(BaseModel):
    nome: str
    email: EmailStr
    celular: str
    senha: str
    endereco: str


class AtualizarCliente(BaseModel):
    id: int
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    celular: Optional[str] = None
    endereco: Optional[str] = None


class ClienteResposta(ClienteSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
