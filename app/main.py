import redis.asyncio as redis
from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi_limiter import FastAPILimiter
import os 

app=FastAPI()
app.include_router(api_router)

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
@app.on_event('startup')
async def startup():
    redis_client=redis.from_url(
        redis_url,
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(redis_client)