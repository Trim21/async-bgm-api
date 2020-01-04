import pytest

from async_bgm_api import BgmApi


@pytest.fixture
@pytest.mark.asyncio
async def api():
    api = BgmApi()
    yield api
    await api.close()


@pytest.fixture
@pytest.mark.asyncio
async def api_mirror():
    api = BgmApi(mirror=True)
    yield api
    await api.close()
