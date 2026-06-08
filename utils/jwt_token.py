from jose import JWTError , jwt
from datetime import timedelta , timezone , datetime
from config.config import settings

def create_access_token(data:dict):

    to_encode = data.copy()

    expire_time_minutes = settings.token_expiry_time_minutes

    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_time_minutes)
    
    to_encode.update({"exp":expire})

    jwt_encoded = jwt.encode(to_encode,settings.secret_key,settings.algorithm)

    return jwt_encoded


def verify_access_token(token:str):

    try:
        print("Token = ",token)
        payload = jwt.decode(token,settings.secret_key,settings.algorithm)
        return payload
    except JWTError:
        return None  

