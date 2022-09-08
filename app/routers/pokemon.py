from fastapi import APIRouter

router = APIRouter()

@router.get("/pokemon", tags=["pokemon"])
async def pokemon():
    return "pika pika"
