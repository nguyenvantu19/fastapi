from typing import List, Optional
from app.models.user import User, UserCreate
from app.db.fake_db import db_users

def get_next_id() -> int:
    return max([u.id for u in db_users], default=0) + 1

def get_users() -> List[User]:
    return db_users

def get_user(user_id: int) -> Optional[User]:
    for u in db_users:
        if u.id == user_id:
            return u
    return None

def add_user(user: UserCreate) -> User:
    new_user = User(id=get_next_id(), **user.dict())
    db_users.append(new_user)
    return new_user

def update_user(user_id: int, user: UserCreate) -> Optional[User]:
    for i, u in enumerate(db_users):
        if u.id == user_id:
            updated_user = User(id=user_id, **user.dict())
            db_users[i] = updated_user
            return updated_user
    return None

def delete_user(user_id: int) -> bool:
    for i, u in enumerate(db_users):
        if u.id == user_id:
            db_users.pop(i)
            return True
    return False
