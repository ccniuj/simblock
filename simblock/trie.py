from .env import Env
from .utils import sha3_256, simple_encode, sort_dict

# Not a real Trie yet!
class Trie():
    def __init__(self, env=Env()):
        self.db = env.state_db

    def get(self, key):
        return self.db.get(key)

    def put(self, key, value):
        return self.db.put(key, value)

    @property
    def root_hash(self):
        return sha3_256(simple_encode(sort_dict(self.db.store)))
