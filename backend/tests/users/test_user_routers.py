import pytest 
from httpx import AsyncClient

from src.users.models import User


@pytest.mark.asyncio
async def test_register_endpoint(async_client: AsyncClient):
    response = await async_client.post('/users/register', json={
        'username': 'test_user',
        'password': '12345678',
        're_password': '12345678'
    })
    assert response.status_code == 200
    assert response.json() == {'username': 'test_user', 'is_active': True, 'id': 1}


@pytest.mark.asyncio 
async def test_login_for_access_token_endpoint(async_client: AsyncClient, test_user: User):
    data = {
        'username': test_user.username,
        'password': '12345678'
    }
    response = await async_client.post('users/login', data=data)
    assert response.status_code == 200
    

@pytest.mark.asyncio 
async def test_me_endpoint(async_client: AsyncClient, test_user: User):
    data = {
        'username': test_user.username,
        'password': '12345678'
    }
    login_response = await async_client.post('users/login', data=data)
    access_token = login_response.json()['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = await async_client.get('users/me', headers=headers)
    assert response.status_code == 200
