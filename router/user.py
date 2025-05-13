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

# Get User
# @router.get("/")
# def index():
#     return {"message": "Hello, User!"}

# @router.get("/all")
# def get_all_users():
#     return {"message": "All users"}

# Get User by ID
