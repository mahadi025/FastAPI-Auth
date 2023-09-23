from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, FLOAT
from sqlalchemy.sql import func
from models import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(30), nullable=True)
    password = Column(String(255), nullable=False)
    log_info = Column(DateTime(timezone=True), default=func.now())


class Student(BaseModel):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_id = Column(String(100), nullable=False, unique=True)
    department = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))



class Grade(BaseModel):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(String(100), ForeignKey("students.student_id"))
    semester = Column(String(10), nullable=False)
    cgpa = Column(FLOAT, nullable=False)