import asyncio
import functools

import httpx

from async_bgm_api.exceptions import ServerConnectionError


def wrap_connection_error(func):
    assert asyncio.iscoroutinefunction(func), f'{func} is not coroutine function'

    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except (httpx.TimeoutException, ConnectionError) as e:
            raise ServerConnectionError(raw_exception=e)

    return wrapped