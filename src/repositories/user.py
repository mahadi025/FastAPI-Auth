from typing import Optional
from repositories import BaseRepo
from schemas import UserIn, UserUpdate
from models import User
from sqlalchemy.orm import Session


class UserRepo(BaseRepo[User, UserIn, UserUpdate]):

    def search_by_email(self, db:Session, email_in:str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email_in).first()


user_repo = UserRepo(User)