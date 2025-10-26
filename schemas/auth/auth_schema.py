from typing import Optional

from pydantic import BaseModel

from schemas.user.user_schema import UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str
    user: Optional[UserResponse] = None