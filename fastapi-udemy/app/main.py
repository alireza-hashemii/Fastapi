from fastapi import FastAPI , HTTPException
from fastapi.responses import JSONResponse , PlainTextResponse
from exceptions import StoryException
from fastapi import status
from fastapi import Request 
from fastapi.middleware import cors
from routers import (blog_get_router , blog_post_router ,
                    user , article_router , product_router , 
                )
from authentication import token_router
from db import models
from db.database import engine
app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get_router.router)
app.include_router(blog_post_router.router)
app.include_router(article_router.router)
app.include_router(product_router.router)
app.include_router(token_router.router)

@app.get('/hello')
def index():
    return {'message':'hello world'}

@app.exception_handler(StoryException)
def exception_handler(request: Request,exc: StoryException):
    return JSONResponse(
        status_code= status.HTTP_418_IM_A_TEAPOT,
        content = {"detail": exc.name}
    )
    
@app.exception_handler(HTTPException)
def custom_handler(request: Request , exc: HTTPException):
    return   PlainTextResponse(
        content= str(exc),
        status_code= status.HTTP_400_BAD_REQUEST
    )

models.Base.metadata.create_all(engine)


# app.add_middleware(
#     cors.CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_method = "*"
#     allow_headers = "*"
# )