from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from db.models import ArticleTable
from exceptions import StoryException

from schemas import ArticleBase 



def create_article(db: Session,request: ArticleBase):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please")
    new_article = ArticleTable(
       title = request.title, 
       content = request.content,
       published = request.published,
       user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    
def retrieve_article(db: Session,id: int):
    article = db.query(ArticleTable).filter(ArticleTable.id==id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with id {id} didn't found"
        )
    return article 


