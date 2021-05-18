from memcache import Client

from main.configs import config


class MemcacheClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _make_key(key):
        return f"{config.CACHE_PREFIX}-{key}"

    def set(self, key, val, time=0, *args, **kwargs):
        super().set(key=self._make_key(key), val=val, time=time, *args, **kwargs)

    def get(self, key):
        super().get(key=self._make_key(key))

    def delete(self, key, *args, **kwargs):
        super().delete(key=self._make_key(key), *args, **kwargs)
