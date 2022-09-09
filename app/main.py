from fastapi import FastAPI
from app.routers import hello, pokemon
from app.infra import db

app = FastAPI()

app.include_router(hello.router)
app.include_router(pokemon.router)

@app.on_event("startup")
async def run_db_migration():
    await db.run_migration()

@app.on_event("shutdown")
async def clean_resources():
    await db.remove_inmemory_db()

@app.get("/")
async def root():
    return {"Status": "All good"}
