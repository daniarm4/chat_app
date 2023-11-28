from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs, AsyncSession

from src.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass 


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
