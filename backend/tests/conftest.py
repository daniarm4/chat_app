from typing import Generator

from asyncio import current_task, get_event_loop_policy

import pytest 
from httpx import AsyncClient
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    async_sessionmaker,
    AsyncSession
)

from src.main import app
from src.config import TEST_DATABASE_URL
from src.database import Base, get_async_session
from src.users.models import User
from src.users.auth import get_password_hash

async_engine = create_async_engine(TEST_DATABASE_URL)
TestingAsyncSession = async_scoped_session(
    session_factory=async_sessionmaker(
        async_engine,
        expire_on_commit=False, 
        autoflush=False
    ),
    scopefunc=current_task
)

async def override_get_async_session() -> Generator[AsyncSession, None, None]:
    async with TestingAsyncSession() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope="session")
def event_loop():
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def db_setup() -> Generator[None, None, None]:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session() -> Generator[AsyncSession, None, None]:
    async with TestingAsyncSession() as session:
        try:
            yield session 
        except:
            session.rollback()
            raise 


@pytest.fixture(scope='session')
def sync_client() -> Generator[TestClient, None, None]:
    yield TestClient(app)


@pytest.fixture(scope='session')
async def async_client() -> Generator[AsyncClient, None, None]:
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as client:
        yield client


@pytest.fixture
async def test_user(db_session: AsyncSession) -> Generator[User, None, None]:
    hash_password = get_password_hash('12345678')
    user = User(
        username='user',
        hashed_password=hash_password,
        is_active=True
    )
    db_session.add(user)
    await db_session.commit()     
    yield user 
    await db_session.delete(user)
    await db_session.commit()
