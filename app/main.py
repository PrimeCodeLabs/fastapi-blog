from fastapi import FastAPI
from app.controllers import user, post
from app.configs.config import settings

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(post.router, prefix="/posts", tags=["posts"])

@app.get("/info")
async def info():
    return {
        "database_url": settings.database_url,
        "secret_key": settings.secret_key,
        "access_token_expire_minutes": settings.access_token_expire_minutes,
    }