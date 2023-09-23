from pydantic import BaseModel
from typing import Optional


class GradeBase(BaseModel):
    cgpa: float
    semester: str


class GradeIn(GradeBase):
    student_id: Optional[str] = None
       

class GradeOut(GradeBase):
    student_id: str
    id: int

    class Config:
        orm_mode = True


class GradeOutStudent(GradeBase):
    id: str

    class Config:
        orm_mode = True


class GradeUpdate(BaseModel):
    semester: str
    cgpa: float