from fastapi import FastAPI
import router

app = FastAPI()
app.include_router(router.router)