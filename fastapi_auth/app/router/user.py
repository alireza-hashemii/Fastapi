from fastapi import APIRouter 

router = APIRouter(
    tags= ['user']
)

@router.get("/")
def retrieve_users():
    pass 

@router.get("/{user_id}")
def retrieve_user():
    pass 

@router.post("/create")
def create_user():
    pass

@router.put("/modify")
def change_user_info():
    pass 