from fastapi import APIRouter
from app.infra import db

router = APIRouter()

@router.get("/hello", tags=["hello"])
async def hello():
    return "hello world"

@router.get("/hello/{last_name}", tags=["hello"])
async def hello_name(last_name):
    user = await db.fetch_user(last_name)
    if user is None:
        return f"Who is this {last_name}??"
    
    return f"hello world {user.first_name} {last_name}"