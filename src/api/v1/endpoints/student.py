from fastapi import APIRouter, Depends
from api.v1.auth_deps import logged_in
from schemas import StudentBase, StudentOut, StudentOutUser, StudentUpdate, ResultIn
from exceptions import handle_result
from sqlalchemy.orm import Session
from db import get_db
from typing import List, Union
from services import student_service

router = APIRouter()


@router.get('/', response_model=List[Union[ResultIn, List[StudentOut]]])
def all_student(skip: int = 0, limit: int = 10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = student_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(all)


@router.post('/', response_model=StudentOut)
def create_student(data_in: StudentBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    student = student_service.create_student(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(student)


@router.get('/user-student/', response_model=List[Union[ResultIn, List[StudentOutUser]]])
def user_student(skip: int = 0, limit: int = 10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    user_id = current_user.id
    all = student_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, user_id=user_id)
    return handle_result(all)


@router.get('/{id}', response_model=StudentOut)
def get_one(id, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    student = student_service.get_one(db, id)
    return handle_result(student)
    

@router.put('/{id}', response_model=StudentOut)
def update_student(id: int, student_update: StudentUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    update = student_service.update(db, id, data_update=student_update)
    return handle_result(update)


@router.delete('/{id}')
def delete_student(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    delete = student_service.delete(db, id=id)
    return handle_result(delete)