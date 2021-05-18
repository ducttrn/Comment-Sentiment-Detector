from main.configs.base import Config


class DevelopmentConfig(Config):
    # Memcached
    MEMCACHED_SERVERS = ["127.0.0.1:11211"]
    CACHE_PREFIX = "sentiment"
    CACHE_TIME_OUT = 3600

    DEBUG = True


config = DevelopmentConfig
