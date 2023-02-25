from ...config.setting import settings
from functools import lru_cache


@lru_cache()
def get_settings():
    return settings
