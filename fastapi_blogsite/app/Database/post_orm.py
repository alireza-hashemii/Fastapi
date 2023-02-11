from sqlalchemy.orm import Session
from Database.models import Post
from router.schemas import PostBase
from datetime import datetime

def create(db: Session,request: PostBase):
    new_post = Post(
    image_url = request.image_url,
    title = request.title,
    content = request.content,
    creator = request.creator,
    timestamp = datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def retrieve(db: Session):
    all_posts = db.query(Post).all()
    if not all_posts:
        return ("There isn't any post")
    return all_posts

    
def delete(db: Session,id: int):
    delete_post = db.query(Post).filter(Post.id == id).first()
    if not delete_post:
        return ("There isn't any post with this id.")
    db.delete(delete_post)
    db.commit()
    return delete_post