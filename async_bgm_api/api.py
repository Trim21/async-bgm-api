from typing import List, Union

import httpx
from httpx.models import HeaderTypes, QueryParamTypes, URLTypes

from async_bgm_api.exceptions import RecordNotFound, ServerConnectionError
from async_bgm_api.models import (
    Calendar,
    CollectionCat,
    SubjectSmall,
    UserCollection,
    UserInfo,
)
from async_bgm_api.models.subject import SubjectLarge, SubjectMedia

REQUEST_SERVICE_USER_AGENT = "async-bgm-api (0.0.1)"

UserID = Union[str, int]


class BgmApi:
    def __init__(self, mirror=False):
        if mirror:
            self.host = "mirror.api.bgm.rin.cat"
        else:
            self.host = "api.bgm.tv"

        self.session = httpx.Client(
            base_url=f"https://{self.host}/",
            headers={"user-agent": REQUEST_SERVICE_USER_AGENT},
        )

    async def get(
        self,
        url: URLTypes,
        *,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ):
        try:
            return await self.session.get(url, params=params, headers=headers)
        except (httpx.TimeoutException, ConnectionError) as e:
            raise ServerConnectionError(raw_exception=e)

    @staticmethod
    def json(response: httpx.Response):
        data = response.json()
        if "error" in data:
            if data["code"] == 404:
                raise RecordNotFound(request=response.request, response=response)
        return data

    async def get_user_info(self, user_id: UserID) -> UserInfo:
        """
        https://bangumi.github.io/api/#/用户/get_user__username_

        :param user_id:
        :return:
        """
        req = await self.get(f"/user/{user_id}")
        data = self.json(req)
        return UserInfo.parse_obj(data)

    async def get_user_collection(
        self, user_id: UserID, cat: CollectionCat,
    ) -> List[UserCollection]:
        """
        https://bangumi.github.io/api/#/用户/get_user__username__collection

        :param user_id:
        :param cat: ``watching`` or ``all_watching``
        :return:
        """
        req = await self.get(f"/user/{user_id}/collection", params={"cat": cat},)
        data = self.json(req)
        return [UserCollection.parse_obj(x) for x in data]

    async def get_user_watching_subjects(self, user_id: UserID) -> List[UserCollection]:
        r = await self.get(f"/user/{user_id}/collection", params={"cat": "watching"})
        data = self.json(r)
        return [UserCollection.parse_obj(x) for x in data]

    async def get_calendar(self) -> List[Calendar]:
        r = await self.get("/calendar")
        data = self.json(r)
        return [Calendar.parse_obj(x) for x in data]

    async def get_subject_small(self, subject_id: int) -> SubjectSmall:
        r = await self.get(f"/subject/{subject_id}", params={"responseGroup": "small"})
        data = self.json(r)
        return SubjectSmall.parse_obj(data)

    async def get_subject_media(self, subject_id: int) -> SubjectMedia:
        """
        ``medium`` should be typo

        :param subject_id:
        :return:
        """
        r = await self.get(f"/subject/{subject_id}", params={"responseGroup": "medium"})
        data = self.json(r)
        return SubjectMedia.parse_obj(data)

    async def get_subject_large(self, subject_id: int) -> SubjectLarge:
        r = await self.get(f"/subject/{subject_id}", params={"responseGroup": "large"})
        data = self.json(r)
        return SubjectLarge.parse_obj(data)
