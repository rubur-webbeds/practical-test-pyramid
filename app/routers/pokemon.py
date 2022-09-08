from fastapi import APIRouter
from app.infra import api

router = APIRouter()

@router.get("/pokemon", tags=["pokemon"])
async def pokemon():
    pika = await api.fetch_pika()
    return pika
