from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from schemas import UserBase
from hash import Hash
from db.models import DbUser

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
        
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def retrieve_all(db: Session):
    return db.query(DbUser).all()
    
def get_user_by_username(db: Session, username: str):
  user = db.query(DbUser).filter(DbUser.username == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with username {username} not found')
  return user

def update_user(db: Session,id: int,request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
            detail= f"User with id {id} Doesn't change"
    )
    user.update({
    DbUser.username : request.username,
    DbUser.email : request.email,
    DbUser.password : Hash.bcrypt(request.password)
    })
    db.commit()
    return "ok"

def user_delete(db: Session,id : int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
            detail= f"User with id {id} Doesn't change"
    )
    db.delete(user)
    db.commit()
    return "ok"
    
def get_user(db: Session, id: int):
    user_instance = db.query(DbUser).filter(DbUser.id == id).first()
    if not user_instance:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail= f"User with id {id} not found"
        )
    return user_instance