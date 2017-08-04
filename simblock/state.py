from .env import Env
from .trie import Trie
from .account import Account
from .block_header import GENESIS_BLOCK_HEADER
# from .block import Block
from .utils import copy

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
            assert len(addr) == 20

            # Set state from alloc
            self.set_account(addr, data)

        return self

    def clone(self):
        return copy(self)

    @property
    def db(self):
        return self.trie.db

    @property
    def root_hash(self):
        return self.trie.root_hash

    def apply_block(self, block):
        # 1. Validate block
        # 2. Apply transactions
        # 3. Reward
        # 4. Verify state root and tansaction root
        # 5. Post-finalize
        assert block.validate()

        for tx in block.transactions:
            self.apply_transaction(tx)

        assert block.verify()
        self.add_block_header(block.header)

    def apply_transaction(self, tx):
        from_addr = tx.sender
        to_addr = tx.tx_data["to"]
        value = tx.tx_data["value"]

        # Increment nonce
        self.increment_nonce(from_addr)

        # Transfer value
        res = self.transfer_value(from_addr=from_addr, to_addr=to_addr, value=value)
        return res

    def transfer_value(self, from_addr=None, to_addr=None, value=None):
        if (not from_addr) or (not to_addr) or (value == 0):
            raise ValueError("Argument 'from'/'to'/'value' is not provided.")

        assert value > 0

        from_acct = self.get_account(from_addr)
        to_acct = self.get_account(to_addr)

        if from_acct.data["balance"] >= value:
            from_acct.data["balance"] -= value
            to_acct.data["balance"] += value
            return True
        else:
            return False

    def increment_nonce(self, addr):
        acct = self.get_account(addr)
        acct.data["nonce"] += 1

    def add_block_header(self, header):
        self.prev_headers = [header] + self.prev_headers
