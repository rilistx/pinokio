from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.settings.config import config


async_engine = create_async_engine(
    url=config.POSTGRES_URL,
    echo=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
