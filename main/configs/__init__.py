import importlib
import os

env = os.getenv("ENVIRONMENT", "development")

config = importlib.import_module("main.configs." + env).config
