from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User, UserCreate
from app.services import user_service

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users():
    return user_service.get_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
def add_user(user: UserCreate):
    return user_service.add_user(user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    updated_user = user_service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Xoá thành công"}
