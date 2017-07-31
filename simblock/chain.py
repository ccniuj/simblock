from .env import Env
from .block_header import GENESIS_BLOCK_HEADER
from .block import Block
# from .state import State

class Chain(object):
    def __init__(self, state=None, env=None):
        self.env = env or Env()

        if state:
            self.state = state
            self.env = state.env

        # Assert if state DB equals to env DB
        assert self.env.db == self.state.db

        # Set genesis block
        self.genesis = Block(header=GENESIS_BLOCK_HEADER)

        # Set head hash
        self.head_hash = self.state.prev_headers[0].hash

    @property
    def head(self):
        if self.head_hash == GENESIS_BLOCK_HEADER.hash:
            return self.genesis
        else:
            pass

    @property
    def db(self):
        return self.env.db
