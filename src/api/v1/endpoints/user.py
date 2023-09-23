from fastapi import APIRouter, Depends
from api.v1.auth_deps import logged_in
from schemas import UserIn, UserOut, UserAuthOut, UserUpdate, ResultIn
from exceptions import handle_result
from sqlalchemy.orm import Session
from db import get_db
from typing import List, Union
from services import user_service, student_service, grade_service

router = APIRouter()

@router.get('/', response_model=List[Union[ResultIn, List[UserOut]]])
def all_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    all = user_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(all)


@router.post('/', response_model=UserOut)
def create_user(data_in: UserIn, db: Session = Depends(get_db)):
    user = user_service.create_user(db=db, data_in=data_in, flush=False)
    return handle_result(user)


@router.get('/{id}', response_model=UserAuthOut)
def get_one(id, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    todo = user_service.get_one(db, id)
    return handle_result(todo)


@router.put('/{id}', response_model=UserOut)
def update_user(id: int, user_update: UserUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    update = user_service.update(db, id, data_update=user_update)
    return handle_result(update)

@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    try:
        student_id = student_service.get_by_key_first(db, user_id=current_user.id).value.id
        delete_student = student_service.delete(db, id=student_id)
        grade_id = grade_service.get_by_key_first(db, student_id=student_id).value.id
        delete_grade = grade_service.delete(db, id=grade_id)
    except:
        pass
    delete = user_service.delete(db, id=id)
    return handle_result(delete)
