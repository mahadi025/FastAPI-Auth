from fastapi import APIRouter

from .endpoints import auth, user, student, grade

api_router = APIRouter()

# fmt: off
api_router.include_router(auth.router, prefix='', tags=['Auth'])
api_router.include_router(user.router, prefix='/users', tags=['Users'])
api_router.include_router(student.router, prefix='/students', tags=['Students'])
api_router.include_router(grade.router, prefix='/grades', tags=['Grades'])