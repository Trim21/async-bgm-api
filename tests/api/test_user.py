import pytest

from async_bgm_api import BgmApi
from async_bgm_api.exceptions import RecordNotFound
from async_bgm_api.models import CollectionCat, UserCollection, UserInfo

non_exists_user_id = "non_exists_user_id"


@pytest.mark.asyncio
async def test_get_user_200(api_mirror: BgmApi):
    r = await api_mirror.get_user_info(3)
    assert isinstance(r, UserInfo)
    await api_mirror.get_user_info("sunyanzi")


@pytest.mark.asyncio
async def test_get_user_404(api_mirror: BgmApi):
    with pytest.raises(RecordNotFound):
        await api_mirror.get_user_info(0)


@pytest.mark.asyncio
async def test_get_user_collection_200(api_mirror: BgmApi):
    r = await api_mirror.get_user_collection(1, cat=CollectionCat.watching)
    assert isinstance(r, list)
    for i in r:
        assert isinstance(i, UserCollection)


@pytest.mark.asyncio
async def test_get_user_collection_404(api_mirror: BgmApi):
    with pytest.raises(RecordNotFound):
        await api_mirror.get_user_collection(
            non_exists_user_id, cat=CollectionCat.watching
        )
