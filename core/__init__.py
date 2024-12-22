__all__ = ['unpacking']


from sqlalchemy import text

from core.database.engine import async_engine


async def unpacking() -> None:
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.first()=}")
