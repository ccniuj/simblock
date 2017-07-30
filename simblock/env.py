from .databases import SimpleDB
default_config = dict()

class Env():
    def __init__(self):
        self.config = default_config
        self.db = SimpleDB()
