import pytest
from app.routers import hello

@pytest.mark.asyncio
async def test_hello_returns_hello_world():
    response = await hello.hello()
    assert response == "hello world"

@pytest.mark.asyncio
async def test_hello_name_returns_full_name(mocker):
    db_user_mock = type('',(object,),{"first_name": "ruben"})()
    mocker.patch('app.routers.hello.db.fetch_user', return_value=db_user_mock)

    expected = "hello world ruben bustos"
    actual = await hello.hello_name(last_name="bustos")
    assert expected == actual