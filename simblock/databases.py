class BaseDB():
    pass

class SimpleDB(BaseDB):
    def __init__(self):
        self.store = {}

    def get(self, key):
        return self.store[key]

    def put(self, key, value):
        self.store[key] = value
        return self.store[key]

    def delete(self, key):
        del self.store[key]
