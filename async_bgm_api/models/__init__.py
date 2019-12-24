from enum import Enum, IntEnum
from typing import Dict, List, Optional

from pydantic import BaseModel

from async_bgm_api.models.subject import (
    SubjectCollection,
    SubjectImage,
    SubjectSmall,
    SubjectType,
)


class CollectionStatusId(int, Enum):
    wish = 1  # 想做
    collect = 2  # 做过
    do = 3  # 在做
    on_hold = 4  # 搁置
    dropped = 5  # 抛弃


class CollectionStatusType(str, Enum):
    wish = "wish"
    collect = "collect"
    do = "do"
    on_hold = "on_hold"
    dropped = "dropped"


class EpisodeType(Enum):
    #: 本篇
    type0 = 0
    #: SP
    special = 1
    op = 2
    ed = 3
    ad = 4
    mad = 5
    other = 6


class StatusEnum(Enum):
    Air = "Air"
    Today = "Today"
    NA = "NA"


class Episode(BaseModel):
    id: int
    url: str
    type: EpisodeType
    sort: int

    name: str
    name_cn: str
    duration: str
    airdate: str
    comment: int
    desc: str
    status: StatusEnum


class SubjectWithEps(BaseModel):
    id: int
    url: str
    type: SubjectType
    name: str
    name_cn: str
    summary: str
    air_date: str
    air_weekday: int
    images: SubjectImage
    eps: List[Episode]


class AuthResponse(BaseModel):
    access_token: str
    expires_in: int
    token_type: str
    scope: Optional[str]
    user_id: int
    refresh_token: str


class UserGroupEnum(IntEnum):
    admin = 1
    bangumi_admin = 2
    window_admin = 3
    quite_user = 4
    banned_user = 5
    character_admin = 8
    wiki_admin = 9
    normal_user = 10
    wiki = 11


class UserInfo(BaseModel):
    id: int
    url: str
    username: str
    nickname: str
    avatar: Dict[str, str]
    sign: str
    usergroup: UserGroupEnum


class RefreshResponse(BaseModel):
    access_token: str
    expires_in: int
    token_type: str
    scope: Optional[str] = ""
    refresh_token: str


class UserCollectionSubject(BaseModel):

    images: SubjectImage
    id: int
    url: str
    type: SubjectType
    summary: str
    name: str
    name_cn: str

    air_weekday: int
    air_date: str

    eps: Optional[int]
    eps_count: Optional[int]
    collection: SubjectCollection


class UserCollection(BaseModel):
    name: str
    subject_id: int
    #: 完成话数
    ep_status: int
    #: 完成话数（书籍）
    vol_status: int
    lasttouch: int
    subject: UserCollectionSubject


class CollectionCat(str, Enum):
    watching = "watching"
    all_watching = "all_watching"


class Weekday(BaseModel):
    en: str
    cn: str
    ja: str
    id: int


class Calendar(BaseModel):
    weekday: Weekday
    items: List[SubjectSmall]
