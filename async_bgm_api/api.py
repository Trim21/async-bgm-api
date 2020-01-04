import urllib
import urllib.parse
from typing import List, Union

import aiohttp

from async_bgm_api.exceptions import RecordNotFound, ServerConnectionError
from async_bgm_api.models import (
    Calendar,
    CollectionCat,
    SubjectSmall,
    SubjectWithEps,
    UserCollection,
    UserInfo,
)
from async_bgm_api.models.subject import SubjectLarge, SubjectMedia

REQUEST_SERVICE_USER_AGENT = "async-bgm-api"

UserID = Union[str, int]


class BgmApi:
    """
    :param mirror: if use mirror ``mirror.api.bgm.rin.cat``
    """

    def __init__(self, mirror=False):
        if mirror:
            self.host = "mirror.api.bgm.rin.cat"
        else:
            self.host = "api.bgm.tv"
        self.base_url = f"https://{self.host}/"

        self.session = None

    def url(self, path):
        return urllib.parse.urljoin(self.base_url, path)

    async def get(
        self, url, *, params=None, headers=None,
    ):
        if not self.session:
            self.session = aiohttp.ClientSession(
                headers={"user-agent": REQUEST_SERVICE_USER_AGENT},
            )
        try:
            async with self.session.get(
                self.url(url), params=params, headers=headers,
            ) as resp:
                return await self.json(resp)
        except aiohttp.ClientConnectionError as e:
            raise ServerConnectionError(raw_exception=e)

    @staticmethod
    async def json(response: aiohttp.ClientResponse):
        data = await response.json()
        if "error" in data:
            if data["code"] == 404:
                raise RecordNotFound(request=response.request_info, response=response)
        return data

    async def get_user_info(self, user_id: UserID) -> UserInfo:
        """
        `<https://bangumi.github.io/api/#/用户/get_user__username_>`_

        :param user_id:
        """
        data = await self.get(f"/user/{user_id}")
        return UserInfo.parse_obj(data)

    async def get_user_collection(
        self, user_id: UserID, cat: CollectionCat,
    ) -> List[UserCollection]:
        """
        `<https://bangumi.github.io/api/#/用户/get_user__username__collection>`_

        :param user_id:
        :param cat: ``watching`` or ``all_watching``
        """
        data = await self.get(f"/user/{user_id}/collection", params={"cat": cat},)
        return [UserCollection.parse_obj(x) for x in data]

    async def get_user_watching_subjects(self, user_id: UserID) -> List[UserCollection]:
        data = await self.get(f"/user/{user_id}/collection", params={"cat": "watching"})
        return [UserCollection.parse_obj(x) for x in data]

    async def get_calendar(self) -> List[Calendar]:
        data = await self.get("/calendar")
        return [Calendar.parse_obj(x) for x in data]

    async def get_subject_small(self, subject_id: int) -> SubjectSmall:
        """get subject info with response group small

        :param subject_id:

        """
        data = await self.get(
            f"/subject/{subject_id}", params={"responseGroup": "small"}
        )
        return SubjectSmall.parse_obj(data)

    async def get_subject_media(self, subject_id: int) -> SubjectMedia:
        """get subject info with response group ``medium``,
        ``medium`` should be typo I guess.

        :param subject_id:

        """
        data = await self.get(
            f"/subject/{subject_id}", params={"responseGroup": "medium"}
        )
        return SubjectMedia.parse_obj(data)

    async def get_subject_large(self, subject_id: int) -> SubjectLarge:
        """
        get subject info with response group large

        :param subject_id:
        """
        data = await self.get(
            f"/subject/{subject_id}", params={"responseGroup": "large"}
        )
        return SubjectLarge.parse_obj(data)

    async def get_subject_with_eps(self, subject_id: int) -> SubjectWithEps:
        """
        `<https://bangumi.github.io/api/#/条目/get_subject__subject_id__ep>`_

        :param subject_id:
        """
        data = await self.get(f"/subject/{subject_id}/ep")
        return SubjectWithEps.parse_obj(data)

    async def close(self):
        await self.session.close()

    async def __aenter__(self) -> "BgmApi":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
