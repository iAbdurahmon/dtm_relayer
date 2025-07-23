import json

from redis.asyncio import Redis

redis_client = Redis.from_url("redis://localhost")


async def get_global_variable(which):
    value = await redis_client.get(which)
    if value is not None:
        value = value.decode('utf-8')
        try:
            value = json.loads(value)  # если это был список
        except json.JSONDecodeError:
            pass
    return value


async def set_global_variable(which, value):
    if isinstance(value, (list, dict)):
        value = json.dumps(value)  # сериализация
    elif not isinstance(value, (str, bytes, int, float)):
        raise ValueError(f"Unsupported type for Redis: {type(value)}")
    await redis_client.set(which, value)


async def clear_global_variable(which):
    await redis_client.delete(which)
