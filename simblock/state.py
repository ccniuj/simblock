from .env import Env
from .trie import Trie
from .account import Account
from .block_header import GENESIS_BLOCK_HEADER
# from .block import Block
# from copy import deepcopy

class State():
    def __init__(self, env=Env()):
        self.env = env
        self.trie = Trie(env=env)
        self.prev_headers = []

    def get_account(self, addr):
        acct = Account(address=addr, env=self.env)
        return acct

    def set_account(self, addr, data):
        acct = self.get_account(addr)
        acct.set_data(data)

    def from_alloc(self, alloc=None):
        if not alloc:
            raise ValueError("Argument 'alloc' is not provided.")

        # Set prev_headers
        self.prev_headers.append(GENESIS_BLOCK_HEADER)

        for addr, data in alloc.items():
            # Length of address must be exactly 20
            # assert len(addr) == 20

            # Set state from alloc
            self.set_account(addr, data)

        return self

    @property
    def db(self):
        return self.env.db
