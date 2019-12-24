from async_bgm_api.api import BgmApi
from pkg_resources import get_distribution

__all__ = ['BgmApi']


__version__ = get_distribution(__package__).version
