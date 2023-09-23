from fastapi import APIRouter, Depends
from api.v1.auth_deps import logged_in
from schemas import GradeBase, GradeOut, GradeOutStudent, GradeUpdate, ResultIn
from exceptions import handle_result
from sqlalchemy.orm import Session
from db import get_db
from typing import List, Union
from services import grade_service, student_service


router = APIRouter()


@router.get('/', response_model=List[Union[ResultIn, List[GradeOut]]])
def all_grade(skip: int = 0, limit: int = 10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = grade_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(all)


@router.post('/', response_model=GradeOut)
def create_grade(data_in: GradeBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    student_id = student_service.get_by_key_first(db, user_id=current_user.id).value.student_id
    grade = grade_service.create_grade(db=db, data_in=data_in, student_id=student_id)
    return handle_result(grade)

# @router.get('/student-grade/', response_model=List[Union[ResultIn, List[GradeOutStudent]]])
# def student_grade(skip: int = 0, limit: int = 10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
#     student = student_service.get_one(db, id)
#     all = grade_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, student_id=student.student_id)
#     return handle_result(all)


@router.get('/{id}', response_model=GradeOut)
def get_one(id, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    grade = grade_service.get_one(db, id)
    return handle_result(grade)
    

@router.put('/{id}', response_model=GradeOut)
def update_grade(id: int, grade_update: GradeUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    update = grade_service.update(db, id=id, data_update=grade_update)
    return handle_result(update)


@router.delete('/{id}')
def delete_grade(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    delete = grade_service.delete(db, id=id)
    return handle_result(delete)