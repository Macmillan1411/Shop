from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine

from app.database.models import Base
from config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
