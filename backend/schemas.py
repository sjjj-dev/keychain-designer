import uuid
from pydantic import BaseModel
import uuid
from typing import List, Optional
from pydantic import BaseModel, EmailStr


# -----------------
# User schemas
# -----------------
class UserBase(BaseModel):
    email: EmailStr
    display_name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# -----------------
# Chain schemas
# -----------------
class ChainBase(BaseModel):
    name: str


class ChainCreate(ChainBase):
    user_id: uuid.UUID


class ChainRead(ChainBase):
    id: uuid.UUID
    user_id: uuid.UUID
    root_id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True


# -----------------
# Ring / Key / Charm schemas
# Keep separate models (your DB uses separate tables).
# -----------------
class RingBase(BaseModel):
    name: str
    color: str
    parent_id: Optional[uuid.UUID] = None


class RingCreate(RingBase):
    chain_id: uuid.UUID


class RingRead(RingBase):
    id: uuid.UUID
    chain_id: uuid.UUID

    class Config:
        orm_mode = True


class KeyBase(BaseModel):
    name: str
    color: str
    parent_id: Optional[uuid.UUID] = None


class KeyCreate(KeyBase):
    chain_id: uuid.UUID


class KeyRead(KeyBase):
    id: uuid.UUID
    chain_id: uuid.UUID

    class Config:
        orm_mode = True


class CharmBase(BaseModel):
    name: str
    type: str
    parent_id: Optional[uuid.UUID] = None


class CharmCreate(CharmBase):
    chain_id: uuid.UUID


class CharmRead(CharmBase):
    id: uuid.UUID
    chain_id: uuid.UUID

    class Config:
        orm_mode = True


# Collection responses
class ListResponse(BaseModel):
    items: List
    total: int
