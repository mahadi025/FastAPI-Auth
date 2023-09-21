from repositories import BaseRepo
from schemas import StudentIn, StudentUpdate 
from models import Student
from sqlalchemy.orm import Session


class StudentRepo(BaseRepo[Student, StudentIn, StudentUpdate]):

    def create_student(self, db:Session, data_in:StudentIn, user_id:int):
        data_for_db = StudentIn(user_id=user_id, **data_in.dict())
        student = self.create(db=db, data_in=data_for_db)
        return student


student_repo = StudentRepo(Student)