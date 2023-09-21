from services import BaseService
from repositories import student_repo
from models import Student
from schemas import StudentIn, StudentUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class StudentService(BaseService[Student, StudentIn, StudentUpdate]):

    def create_student(self, db:Session, data_in:StudentIn, user_id:int):
        student = self.repo.create_student(db=db, data_in=data_in, user_id=user_id)
        if not student:
            return ServiceResult(AppException.ServerError("Student not created!"))
        else:
            return ServiceResult(student, status_code=status.HTTP_201_CREATED)



student_service = StudentService(Student, student_repo)