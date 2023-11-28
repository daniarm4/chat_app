from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.users.models import User
from src.users.schemas import UserCreate
from src.users.auth import get_password_hash


def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    hashed_password = get_password_hash(user_create.password.get_secret_value())
    user = User(
        username=user_create.username,
        hashed_password=hashed_password
    )
    session.add(user)
    return user 


async def get_user_by_username_or_none(session: AsyncSession, username: str) -> User | None:
    query = select(User).where(User.username==username)
    user = await session.scalar(query)
    return user


async def get_user_by_id_or_none(session: AsyncSession, user_id: str) -> User | None:
    user = await session.get(User, user_id)
    return user
