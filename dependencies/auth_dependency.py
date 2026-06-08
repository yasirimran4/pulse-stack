from database.session import SessionLocal
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends , HTTPException ,status
from sqlalchemy.orm import Session
from utils.jwt_token import verify_access_token
from models.user import User

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
        finally:
            await session.close()    

security = HTTPBearer()

def get_current_user(credentials :HTTPAuthorizationCredentials = Depends(security),db : Session=Depends(get_db)):
    
    token = credentials.credentials
    
    payload = verify_access_token(token)

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
           detail="User not found")
    
    return user

