from typing import List

import pytest

from async_bgm_api import BgmApi
from async_bgm_api.models import SubjectWithEps
from async_bgm_api.models.subject import SubjectLarge, SubjectMedia, SubjectSmall

subject_id = 8


@pytest.mark.asyncio
async def test_get_calendar(api_mirror: BgmApi):
    r = await api_mirror.get_calendar()
    assert isinstance(r, List)


@pytest.mark.asyncio
async def test_get_subject_small(api_mirror: BgmApi):
    r = await api_mirror.get_subject_small(subject_id)
    assert isinstance(r, SubjectSmall)


@pytest.mark.asyncio
async def test_get_subject_media(api_mirror: BgmApi):
    r = await api_mirror.get_subject_media(subject_id)
    assert isinstance(r, SubjectMedia)


@pytest.mark.asyncio
async def test_get_subject_large(api_mirror: BgmApi):
    r = await api_mirror.get_subject_large(subject_id)
    assert isinstance(r, SubjectLarge)


@pytest.mark.asyncio
async def test_get_subject_with_ep_200(api_mirror: BgmApi):
    r = await api_mirror.get_subject_with_eps(subject_id)
    assert isinstance(r, SubjectWithEps)
