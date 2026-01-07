from fastapi import FastAPI
from app.api.transaction import router

app = FastAPI(title="SentinelStream")

app.include_router(router)
