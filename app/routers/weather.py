from fastapi import APIRouter

router = APIRouter()

@router.get("/weather", tags=["weather"])
async def weather():
    return "freezing cold"
