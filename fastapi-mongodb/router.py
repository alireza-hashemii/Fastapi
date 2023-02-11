from fastapi import APIRouter
from repository import BookRepo
from model import Book, Response


router = APIRouter()

@router.get("/book/")
async def retrieve_books():
    _booklist = await BookRepo.retrieve()
    return Response(code=200,status="ok",message="succesful book retrieve",result=_booklist).dict(exclude_none=True)

@router.get("/create/")
async def create(book:Book):
    try:
        await BookRepo.insert(book)
        return Response(code=200,status="ok",message="succesful insert book").dict(exclude_none=True)
    except:
        return "Error"
@router.get("/book/{id}")
async def book_id(id: str):
    _book = await BookRepo.retrieve_id(id)
    return Response(code=200,status="ok",message="succesful retrieve data",result=_book).dict(exclude_none=True)

    
@router.post("/book/update/{id}")
async def update(book: Book,id: str):
    await BookRepo.update(id=id,book=book)
    return Response(code=200,status="ok",message="succesful update data").dict(exclude_none=True)


@router.delete("/book/delete")
async def delete(id: str):
    await BookRepo.delete(id)
    return Response(code=200,status="ok",message="succesful delete data").dict(exclude_none=True)
