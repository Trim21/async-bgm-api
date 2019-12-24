import pytest

from async_bgm_api import BgmApi


@pytest.fixture
def api():
    yield BgmApi()


@pytest.fixture
def api_mirror():
    yield BgmApi(mirror=True)
