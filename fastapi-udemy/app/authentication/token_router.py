from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from hash import Hash
from authentication import oauth2

router = APIRouter(
  tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
  
  access_token = oauth2.create_access_token(data={'sub': user.username})

  return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_id': user.id,
    'username': user.username
  }