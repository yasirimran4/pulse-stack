from fastapi import APIRouter, Depends
from schemas.auth import UserRegister , UserLogin , TokenResponse
from services.auth_service import register_user ,login_user
from dependencies.auth_dependency import get_db
from sqlalchemy.orm import Session
db = get_db()  # Global db for all operations

auth_router = APIRouter(prefix='/api/auth',tags=['Auth'])

@auth_router.post('/register',status_code=201)
def register(user : UserRegister,db : Session = Depends(get_db)):
    return register_user(user,db)

@auth_router.post('/login',status_code=200,response_model=TokenResponse)
def login(user:UserLogin,db : Session = Depends(get_db)):
    return login_user(user,db)  