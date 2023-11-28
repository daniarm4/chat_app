import pytest 

from src.users.service import create_user, get_user_by_username_or_none
from src.users.schemas import UserCreate


@pytest.mark.asyncio
async def test_create_user(db_session):
    new_user = UserCreate(
        username='test_user',
        password='12345678',
        re_password='12345678'
    )
    created_user = create_user(db_session, new_user)
    assert created_user 


@pytest.mark.asyncio
async def test_get_user(db_session, test_user):
    user = await get_user_by_username_or_none(db_session, username=test_user.username)
    assert user 
    assert user.username == test_user.username
