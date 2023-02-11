from fastapi import FastAPI
from router.main_routes import router as router_api

def get_application():
    """ start, configure and return the app """
    application = FastAPI()
    application.include_router(router_api)
    return application

app = get_application()