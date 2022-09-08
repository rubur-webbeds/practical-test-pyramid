import httpx

pokeapi = httpx.Client(base_url="https://pokeapi.co/api/v2")

async def fetch_pika():
    pika = pokeapi.get("/pokemon/pikachu")
    return pika.json()["name"]