import pickle

from pymemcache.client.base import Client

from main.configs import config


class MemcacheClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _make_key(key):
        return f"{config.CACHE_PREFIX}-{pickle.dumps(key.replace(' ', '$'))}"

    def set(self, key, value, time=0, *args, **kwargs):
        super().set(key=self._make_key(key), value=value, expire=time, *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return super().get(key=self._make_key(key), *args, **kwargs)


memcache_client = MemcacheClient(server=config.MEMCACHED_SERVER)
