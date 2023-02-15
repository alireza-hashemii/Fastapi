from fastapi import FastAPI ,Request ,Form,Depends,status
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import engine ,get_db
import models
from starlette.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(request:Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("index.html",{"request":request,"todo_list":todos})


@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)