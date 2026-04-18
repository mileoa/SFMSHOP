# Кеширование
class Cashing:
    def __init__(self):
        self._cache = {}

    def get(self, key):
        return self._cache[key]

    def update(self, key, value):
        self._cache[key] = value

    def has(self, key):
        return key in self._cache
