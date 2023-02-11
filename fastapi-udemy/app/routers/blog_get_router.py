from fastapi import APIRouter
from fastapi import status ,Response
from enum import Enum
from typing import Optional

router = APIRouter(
    tags= ['blog'] ,
    prefix= '/blog'
)


@router.get('/comment/{comment_id}-{blog_id}',tags=['comment'],description="""
        comment id for finding specific comment
        blog id for recognize comment related to witch blog 
        valid is for checking the request
        and username is an optional choice 
         
        """,summary='Comment Api')
def get_comment(comment_id: int,blog_id: int,valid:bool=True,username:Optional[str]=None):
    return {'message':f"comment with id {comment_id} of blog {blog_id} was found - {valid} - {username}"}


@router.get('/all')
def all_blogs(page=1,page_size:Optional[int] = None ):
    """
    simple summary using docstring
    """
    return {"message":f"{page} blogs in page {page_size} provided"}


class BlogTypes(str,Enum):
    short = 'short'
    howto = 'howto'
    lowlevel = 'lowlevel'
    
@router.get('/{type}')
def get_blog(type: BlogTypes):
    return {'message':f"blog with id {type}"}


@router.get('/each/{id}',status_code=status.HTTP_200_OK,response_description='response body')
def blog(id: int ,response : Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message":f"Blog with id {id} found"}