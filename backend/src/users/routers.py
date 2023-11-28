from typing import Annotated

from fastapi import APIRouter, Depends, Security
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.users.auth import (
    authenticate_user, 
    create_access_token, 
    get_current_user, 
    create_refresh_token,
    refresh_security
)
from src.users.schemas import Tokens, UserRead, UserCreate, AccessToken, UserLogin
from src.users.exceptions import UserAlreadyExistsException, UserNotFoundException, UserIsUnauthorized
from src.users.service import create_user, get_user_by_username_or_none
from src.users.models import User 

router = APIRouter(prefix='/users')


@router.post('/login', response_model=Tokens)
async def login(
    user_login: UserLogin,
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    user = await authenticate_user(
        user_login.username, user_login.password.get_secret_value(), session
    )
    if not user:
        raise UserNotFoundException()
    access_token = create_access_token(
        subject={'username': user.username}
    )
    refresh_token = create_refresh_token(
        subject={'username': user.username}
    )
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.post('/refresh', response_model=AccessToken)
async def refresh(
    credentials: Annotated[JwtAuthorizationCredentials, Security(refresh_security)]
):
    if not credentials:
        raise UserIsUnauthorized()
    access_token = create_access_token(subject=credentials.subject)
    return {'access_token': access_token}


@router.post('/register', response_model=UserRead)
async def register(
    user_create: UserCreate, 
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    user = await get_user_by_username_or_none(session=session, username=user_create.username)
    if user:
        raise UserAlreadyExistsException()
    new_user = create_user(session=session, user_create=user_create)
    await session.commit()
    return new_user


@router.get('/me', response_model=UserRead) 
async def me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.get('/{username}', response_model=UserRead)
async def get_user_by_username(
    username: str,
    session: Annotated[AsyncSession, Depends(get_async_session)]):
    user = await get_user_by_username_or_none(session=session,
                                              username=username)
    if not user:
        raise UserNotFoundException()
    return user
