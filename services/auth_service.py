from models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException ,status
from utils.security import hash_password , verify_password
from utils.jwt_token import create_access_token
from config.config import settings

def register_user(user,session:Session):

    existing_user = session.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400,detail="User already registered")
    
    hashed_password = hash_password(user.password)

    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hashed_password
    )
    
    session.add(new_user)

    session.commit()

    session.refresh(new_user)

    return user

def login_user( user,session:Session):

    existing_user = session.query(User).filter(User.email == user.email).first()

    print(existing_user)

    if not existing_user:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email"
        )
    
    is_user = verify_password(user.password,existing_user.hashed_password)
    
    if not is_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password is wrong! try Again")
    
    access_token = create_access_token({"sub":str(existing_user.id)})

    return {"access_token" : access_token,"token_type" : "bearer" ,"expires_in" : settings.token_expiry_time_minutes * 60}
    
    


