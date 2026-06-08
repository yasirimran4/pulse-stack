from fastapi import APIRouter , Depends
from models.user import User
from dependencies.auth_dependency import get_current_user
user_router = APIRouter(prefix='/api/users',tags=['Dashboard'])

@user_router.get("/me")
def get_current_user(current_user:User = Depends(get_current_user)):
     
     return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
