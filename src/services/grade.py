from services import BaseService
from repositories import grade_repo
from models import Grade
from schemas import GradeIn, GradeUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class GradeService(BaseService[Grade, GradeIn, GradeUpdate]):

    def create_grade(self, db:Session, data_in:GradeIn, student_id:str):
        grade = self.repo.create_grade(db=db, data_in=data_in, student_id=student_id)
        if not grade:
            return ServiceResult(AppException.ServerError("Grade not created!"))
        else:
            return ServiceResult(grade, status_code=status.HTTP_201_CREATED)



grade_service = GradeService(Grade, grade_repo)