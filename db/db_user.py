from sqlalchemy.orm import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase

def create_user(db: Session, request: UserBase):
  user_name = DbUser(
    username=request.username,
    email=request.email,
    password=Hash.bcrypt(request.password)
  )
  db.add(user_name)
  db.commit()
  db.refresh(user_name)
  return user_name