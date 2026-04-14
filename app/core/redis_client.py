import json
import os
from typing import Any

from redis import Redis
from redis.exceptions import RedisError


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
_redis_client = Redis.from_url(REDIS_URL, decode_responses=True)


def get_json(key: str) -> Any | None:
    try:
        raw_value = _redis_client.get(key)
    except RedisError:
        return None

    if not raw_value:
        return None

    try:
        return json.loads(raw_value)
    except json.JSONDecodeError:
        return None


def set_json(key: str, value: Any, ttl_seconds: int = 60) -> None:
    try:
        _redis_client.setex(key, ttl_seconds, json.dumps(value))
    except RedisError:
        return


def delete_key(key: str) -> None:
    try:
        _redis_client.delete(key)
    except RedisError:
        return
