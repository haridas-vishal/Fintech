from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.redis import redis_client
from app.services.transaction_service import process_transaction

router = APIRouter(prefix="/transaction")

@router.post("/")
async def create_transaction(
    txn: dict,
    idempotency_key: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    cached = await redis_client.get(idempotency_key)
    if cached:
        return {"status": cached}

    status, risk = await process_transaction(txn, [])

    await redis_client.set(idempotency_key, status, ex=300)
    return {"status": status, "risk_score": risk}

