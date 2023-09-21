from fastapi import APIRouter

from .endpoints import auth, user, student

api_router = APIRouter()

# fmt: off
api_router.include_router(auth.router, prefix='', tags=['Auth'])
api_router.include_router(user.router, prefix='/users', tags=['Users'])
api_router.include_router(student.router, prefix='/students', tags=['Students'])