from typing import Optional , TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class Book(BaseModel):
    id: str = None
    title: str
    description: str

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]