from fastapi import APIRouter, Depends
from schemas.auth import UserRegister , UserLogin , TokenResponse
from services.auth_service import register_user ,login_user
from dependencies.auth_dependency import get_db
from sqlalchemy.ext.asyncio import AsyncSession
db = get_db()  # Global db for all operations

auth_router = APIRouter(prefix='/api/auth',tags=['Auth'])

@auth_router.post('/register',status_code=201)
async def register(user : UserRegister,db : AsyncSession = Depends(get_db)):
    return await register_user(user,db)

@auth_router.post('/login',status_code=200,response_model=TokenResponse)
async def login(user:UserLogin,db : AsyncSession = Depends(get_db)):
    return await login_user(user,db)  