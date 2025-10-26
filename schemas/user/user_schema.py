from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class UserSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone: str


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class UserResponse(CreateUser):
    id: UUID

    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
