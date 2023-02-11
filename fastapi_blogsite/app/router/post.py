from fastapi import APIRouter , Depends , UploadFile, File
from router.schemas import PostBase
from Database.database import get_db
from sqlalchemy.orm import Session
from Database.post_orm import create , retrieve , delete
import random
import shutil
import string

router = APIRouter(
    prefix="/post",
    tags=["post"]
)

@router.get("/retrieve")
def _retrieve(db: Session = Depends(get_db)):
    all_posts = retrieve(db)
    return all_posts

@router.post("/create")
def _create(request: PostBase,db: Session = Depends(get_db)):
    new_post = create(db,request)
    return new_post

@router.delete("/delete/{post_id}")
def _delete(id: int,db: Session = Depends(get_db)):
    deleted_post = delete(db,id)
    return ("Deleted succesfully!")

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
  letter = string.ascii_letters
  rand_str = ''.join(random.choice(letter) for i in range(6))
  new = f'_{rand_str}.'
  filename = new.join(image.filename.rsplit('.', 1))
  path = f'images/{filename}'

  with open(path, "w+b") as buffer:
    shutil.copyfileobj(image.file, buffer)

  return {'filename': path}