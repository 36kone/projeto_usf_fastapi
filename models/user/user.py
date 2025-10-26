from sqlalchemy import Column, String, TIMESTAMP, func

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)