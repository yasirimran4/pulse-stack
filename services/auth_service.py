from models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException ,status
from utils.security import hash_password , verify_password
from utils.jwt_token import create_access_token
from config.config import settings
from sqlalchemy import select

async def register_user(request, session:AsyncSession):

    result = await session.execute(select(User).where(User.email == request.email))
    existing_user = result.scalars().first()

    
    if existing_user:
        raise HTTPException(status_code=400,detail="User already registered")
    
    hashed_password = hash_password(request.password)

    user = User(
        name = request.name,
        email = request.email,
        hashed_password = hashed_password
    )
    
    session.add(user)

    await session.commit()

    await session.refresh(user)

    return user

async def login_user( request,session:AsyncSession):

    result = await session.execute(select(User).where(User.email == request.email))
    user = result.scalars().first()


    if not user:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email"
        )
    
    is_verify = verify_password(request.password,user.hashed_password)
    
    if not is_verify:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password is wrong! try Again")
    
    access_token = create_access_token({"sub":str(user.id)})

    return {"access_token" : access_token,"token_type" : "bearer" ,"expires_in" : settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60}
    
    


