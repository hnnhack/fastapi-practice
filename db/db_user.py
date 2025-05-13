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


def get_all_users(db: Session):
  users = db.query(DbUser).all()
  return users

def get_user(db: Session, user_id: int):
  user = db.query(DbUser).filter(DbUser.id == user_id).first()
  return user

def update_user(db: Session, user_id: int, request: UserBase):
  user = db.query(DbUser).filter(DbUser.id == user_id)
  user.update({
    DbUser.username: request.username,
    DbUser.email: request.email,
    DbUser.password: Hash.bcrypt(request.password)
  })
  db.commit()
  return user.first()
  

def delete_user(db: Session, user_id: int):
  user = db.query(DbUser).filter(DbUser.id == user_id).first()
  db.delete(user)
  db.commit()
  return "User deleted" 