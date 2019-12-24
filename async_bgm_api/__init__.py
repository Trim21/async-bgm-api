from pkg_resources import get_distribution

from async_bgm_api.api import BgmApi

__version__ = get_distribution(__package__).version
__all__ = ["BgmApi"]
