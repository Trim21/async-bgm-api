from enum import Enum
from typing import List, Union

from pydantic import AnyHttpUrl, BaseModel


class SubjectType(Enum):
    book = 1
    anime = 2
    music = 3
    game = 4
    real = 6


class SubjectImage(BaseModel):
    large: str
    common: str
    medium: str
    small: str
    grid: str


class SubjectCollection(BaseModel):
    wish: int = 0
    collect: int = 0
    doing: int = 0
    on_hold: int = 0
    dropped: int = 0


class Rating(BaseModel):
    total: int
    count: dict
    score: float


class SubjectLarge(BaseModel):
    id: int
    url: AnyHttpUrl
    type: SubjectType
    name: str
    name_cn: str
    summary: str
    air_date: str
    air_weekday: int
    images: SubjectImage = None


class SubjectSmall(SubjectLarge):
    eps_count: int = None
    rating: Rating = None
    rank: int = None
    collection: SubjectCollection = None


class CharacterImage(BaseModel):
    large: str
    medium: str
    small: str
    grid: str


class MonoAlias(BaseModel):
    jp: str = None
    kana: str = None
    romaji: str = None
    zh: str = None


class MonoInfo(BaseModel):
    birth: str = None
    height: str = None
    gender: str = None
    alias: MonoAlias = None
    source: Union[str, List[str]] = None
    name_cn: str
    cv: str = None


class MonoBase(BaseModel):
    id: int
    url: str
    name: str
    images: CharacterImage = None


class Character(BaseModel):
    id: int
    url: str
    name: str
    images: CharacterImage = None
    name_cn: str
    comment: int
    collects: int
    info: MonoInfo
    actors: List[MonoBase]
    role_name: str


class Staff(BaseModel):
    id: int
    url: str
    name: str
    images: CharacterImage = None
    name_cn: str
    comment: int
    collects: int
    info: MonoInfo
    role_name: str
    jobs: List[str]


class SubjectMedia(SubjectSmall):
    crt: List[Character]
    staff: List[Staff]
