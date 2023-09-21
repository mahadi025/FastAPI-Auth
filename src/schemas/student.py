from pydantic import BaseModel
from typing import Optional


class StudentBase(BaseModel):
    student_id: str
    department: str


class StudentIn(StudentBase):
    user_id: Optional[int] = None
       

class StudentOut(StudentBase):
    user_id: int
    id: int

    class Config:
        orm_mode = True


class StudentOutUser(StudentBase):
    id: int

    class Config:
        orm_mode = True


class StudentUpdate(BaseModel):
    department: str