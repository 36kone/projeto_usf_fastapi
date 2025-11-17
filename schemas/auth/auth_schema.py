from typing import Optional

from pydantic import BaseModel

from schemas.Cliente.cliente_schema import ClienteResposta


class Token(BaseModel):
    access_token: str
    token_type: str
    user: Optional[ClienteResposta] = None