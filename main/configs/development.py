import os

from main.configs.base import Config


class DevelopmentConfig(Config):
    # Memcached
    MEMCACHED_SERVER = (os.getenv("MEMCACHED_HOST", "localhost"), 11211)
    CACHE_PREFIX = "sentiment"
    CACHE_TIME_OUT = 3600

    TRAINING_LANGUAGE = "vi"


config = DevelopmentConfig
