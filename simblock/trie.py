from .env import Env

class Trie():
    def __init__(self, env=Env()):
        self.db = env.db

    def get(self, key):
        return self.db.get(key)

    def put(self, key, value):
        return self.db.put(key, value)
