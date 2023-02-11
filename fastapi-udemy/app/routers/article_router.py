from typing import List
from fastapi import APIRouter, Depends
from schemas import *
from authentication.oauth2 import oauth2_scheme
from authentication.oauth2 import get_current_user
from db.database import get_db
import orm_article
from schemas import UserBase
from sqlalchemy.orm import Session

router = APIRouter(
    prefix= '/article',
    tags= ['article']
)

@router.post('/create', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return orm_article.create_article(db, request)
    
@router.get("/retrieve/{id}") #response_model=ArticleDisplay)
def retrieve_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        "data": orm_article.retrieve_article(db, id),
        "user": current_user
    }