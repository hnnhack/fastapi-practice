from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from db import db_user
from db.database import get_db

from schemas import UserBase, UserDisplay

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Create User
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# get all users
@router.get("/", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Get User by ID
@router.get("/{user_id}", response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user(db, user_id)
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return user

# Update User
@router.put("/{user_id}", response_model=UserDisplay)
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db_user.get_user(db, user_id)
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return db_user.update_user(db, user_id, request)

# Delete User
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user(db, user_id)
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return db_user.delete_user(db, user_id)

