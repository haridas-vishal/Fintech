import asyncio
from app.core.database import engine, Base
from app.model import user, transaction, fraud_rule, idempotency

async def create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create())
