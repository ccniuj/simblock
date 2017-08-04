from .env import Env
from .block_header import GENESIS_BLOCK_HEADER
from .block import Block
from .utils import simple_encode
# from .state import State

class Chain(object):
    def __init__(self, state=None, env=None):
        self.env = env or Env()

        if state:
            self.state = state
            self.env = state.env

        # Assert if state DB equals to env DB
        assert self.env.state_db == self.state.db

        # Set head hash
        self.head_hash = self.state.prev_headers[0].hash

        # Set genesis block
        self.genesis = Block(header=GENESIS_BLOCK_HEADER)

        try:
            self.db.get(self.genesis.header.hash)
        except KeyError:
            self.db.put(self.genesis.header.hash, simple_encode(dict(self.genesis)))

    @property
    def head(self):
        if self.head_hash == GENESIS_BLOCK_HEADER.hash:
            return self.genesis
        else:
            return self.db.get(self.head_hash)

    @property
    def db(self):
        return self.env.block_db

    def add_block(self, block):
        if block.header.prevhash == self.head_hash:
            self.state.apply_block(block)
            self.head_hash = block.header.hash

        self.db.put(block.header.hash, block)
        return True
