from fastapi import FastAPI
from routes.auth import auth_router
from routes.user import user_router
import uvicorn

app = FastAPI(title="Auth Application",version="1.0.1")

app.include_router(auth_router)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0',port=8000,reload=True )