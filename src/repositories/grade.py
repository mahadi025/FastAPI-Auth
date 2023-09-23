from repositories import BaseRepo
from schemas import GradeIn, GradeUpdate 
from models import Grade
from sqlalchemy.orm import Session


class GradeRepo(BaseRepo[Grade, GradeIn, GradeUpdate]):

    def create_grade(self, db:Session, data_in:GradeIn, student_id:str):
        data_for_db = GradeIn(student_id=student_id, **data_in.dict())
        grade = self.create(db=db, data_in=data_for_db)
        return grade


grade_repo = GradeRepo(Grade)