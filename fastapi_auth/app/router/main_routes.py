from fastapi import APIRouter
from . import user

router = APIRouter()

def include_api_routes():
    """Include to router all api rest routes with version prefix"""
    router.include_router(user.router)

    