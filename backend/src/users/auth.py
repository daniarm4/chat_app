from typing import Annotated 
from datetime import timedelta 

from fastapi_jwt import JwtAccessBearer, JwtRefreshBearer, JwtAuthorizationCredentials
from fastapi import Depends, Security
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from src.config import JWT_SECRET_KEY
from src.database import get_async_session
from src.users.models import User
from src.users.exceptions import UserIsUnauthorized

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
access_security = JwtAccessBearer(
    secret_key=JWT_SECRET_KEY,
    auto_error=False,
    access_expires_delta=timedelta(minutes=15)
)
refresh_security = JwtRefreshBearer(
    secret_key=JWT_SECRET_KEY,
    auto_error=False,
    refresh_expires_delta=timedelta(days=2)
)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

    
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def get_user(username: str,
                   session: AsyncSession) -> User | None:
    query = select(User).where(User.username==username)
    user = await session.scalar(query)
    return user


async def authenticate_user(username: str, password: str, session: AsyncSession) -> User | None:
    user = await get_user(username, session)
    if not user or not verify_password(password, user.hashed_password):
        return None 
    return user


def create_access_token(subject: dict) -> str:
    access_token = access_security.create_access_token(subject=subject)
    return access_token


def create_refresh_token(subject: dict) -> str:
    refresh_token = refresh_security.create_refresh_token(subject=subject)
    return refresh_token


async def get_current_user(credentials: Annotated[JwtAuthorizationCredentials, Security(access_security)],
                           session: Annotated[AsyncSession, Depends(get_async_session)]) -> User:
    if not credentials:
        raise UserIsUnauthorized()
    username = credentials['username']
    user = await get_user(username, session)
    if not user:
        raise UserIsUnauthorized()
    return user
