from database.session import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException ,status
from sqlalchemy.orm import Session
from utils.jwt_token import verify_access_token
from models.user import User
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()    

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

def get_current_user(token:str = Depends(oauth_scheme),db : Session=Depends(get_db)):
    
    payload = verify_access_token(token)

    print("Payload : " , payload)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user_id = payload.get("sub","")

    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
           detail="user not found")
    
    return user

