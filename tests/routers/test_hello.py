import pytest
from app.routers import hello

@pytest.mark.asyncio
async def test_hello_returns_hello_world():
    response = await hello.hello()
    assert response == "hello world"