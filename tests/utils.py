class MockMemcache:
    def __init__(self):
        self.storage = {}

    def set(self, key, value, **__):
        self.storage[key] = value

    def get(self, key):
        return self.storage.get(key)


mocked_memcache = MockMemcache()
