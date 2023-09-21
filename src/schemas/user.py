from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    created_at: Optional[datetime] = None
    log_info: Optional[datetime] = None
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None


class UserPasswordUpdate(BaseModel):
    password: str


class UserAuthOut(UserBase):
    created_at: Optional[datetime] = None
    log_info: Optional[datetime] = None
    id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    identifier: str
    password: str


class ResultIn(BaseModel):
    results: int

    class Config:
        orm_mode = True