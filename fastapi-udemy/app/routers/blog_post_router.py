from typing import Dict, List, Optional
from fastapi import APIRouter , Query , Body ,Path
from pydantic import BaseModel
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Example(BaseModel):
    username : str
    number_comments : int
    published : Optional[bool] 
    follower : Optional[list[str]] 
    mydict : Dict[str,str] = {} 
    
    
@router.post('/new/{id}')
def create_blog(blog:Example ,id: int,version: int=1,):
    return {'data':blog,
            'id':id,
            'version':version
            }
    
@router.post('/new/{id}/comment')
def create_comment(blog: Example , id : int, comment_id: int = Query( None ,   
            title='about id of comment',
            description="Enter it's id here",
            alias='commentId',           
        )):   
    return {
        'blog':blog,
        'id':id,
        'comment_id':comment_id,
    }

@router.post("/new/user/{id}")
def new_user(id: int = Path(None,gt=5,lt=10),username: str = Body(Ellipsis,
    min_length=7,
    max_length= 50,
    description= ' TEST FOR LEARNING'
),content: str = Body('something',regex="^[a-z\s]*$"),version: Optional[List[str]] = Query(default=["1.0","1.2","1.3"])):
    return {
        "id": id,
        "username":username,
        "content":content,
        "version":version
    }
    
