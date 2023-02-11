from typing import List
from fastapi import APIRouter , Depends
from db.models import DbUser
from schemas import UserBase, UserDisplay
from db.database import get_db
import orm_user
from fastapi.security.oauth2 import OAuth2PasswordRequestForm , OAuth2PasswordRequestFormStrict
from sqlalchemy.orm import Session
from orm_user import create_user, update_user

router = APIRouter(
    prefix= '/user',
    tags= ['user']
)

@router.post("/",response_model = UserDisplay)
def user(request: UserBase,db: Session = Depends(get_db)):
    return create_user(db,request)

@router.get("/",response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return orm_user.retrieve_all(db)
    
@router.post("/update/{id}")
def update_user_detail(id: int,request: UserBase,db: Session = Depends(get_db)):
    return orm_user.update_user(db,id,request)

@router.post("/delete/{id}")
def delete(id: int,db: Session = Depends(get_db)):
    return orm_user.user_delete(db,id)

@router.post("/search/{id}")
def user_instance(id: int,db: Session = Depends(get_db)):
    return orm_user.get_user(db,id)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestFormStrict = Depends()):
    data = form_data.parse()
    print(data.username)
    print(data.password)
    for scope in data.scopes:
        print(scope)
    if data.client_id:
        print(data.client_id)
    if data.client_secret:
        print(data.client_secret)
    return data                        