from fastapi import FastAPI
from app.routers import hello, pokemon
from app.infra import db

app = FastAPI()

app.include_router(hello.router)
app.include_router(pokemon.router)

@app.on_event("startup")
async def database_connect():
    await db.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await db.disconnect()

@app.get("/")
async def root():
    return {"Status": "All good"}
