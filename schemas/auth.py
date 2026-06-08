from pydantic import BaseModel,Field ,EmailStr 
from typing import Annotated ,Literal

class UserRegister(BaseModel):
    name : Annotated[str,Field(...,min_length=3,max_length=50,description="Name of user")]
    email :  Annotated[EmailStr,Field(...,description="Email of user")]
    password : Annotated[str,Field(...,min_length=3,max_length=20,description="Password of user")]

class UserLogin(BaseModel):
    email :  Annotated[EmailStr,Field(...,min_length=3,max_length=50,description="Email of user")]
    password : Annotated[str,Field(...,min_length=3,max_length=20,description="Password of user")]
    role : Annotated[Literal["user","admin"],Field(...,description="Role of user")]

class TokenResponse(BaseModel):
    access_token : str
    token_type : str
    expires_in : int  # in  seconds
