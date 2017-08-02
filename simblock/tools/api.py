from simblock.utils import sha3_256, privkey_to_addr
from simblock.state import State
from simblock.env import Env
from simblock.chain import Chain
from simblock.block import Block
from simblock.block_header import BlockHeader
from simblock.transaction import Transaction

class API():
    def __init__(self):
        env = Env()
        self.privkeys = self.make_privkeys()
        alloc = self.make_alloc(self.privkeys)
        state = State(env=env).from_alloc(alloc)
        chain = Chain(state=state, env=env)
        self.chain = chain
        self.block = Block(BlockHeader()).from_prevstate(state=state)
        self.local_state = self.chain.state.clone()

    def make_alloc(self, privkeys):
        default_data = { "balance": 10**24, "nonce": 123 }

        addrs = [privkey_to_addr(key) for key in privkeys]
        alloc = { addr: dict(default_data) for addr in addrs }
        return alloc

    def make_privkeys(self):
        return [sha3_256(i) for i in range(0, 3)]

    @property
    def default_sender_privkey(self):
        return self.privkeys[0]

    @property
    def default_tx_data(self):
        data = {
            "nonce": 0,
            "to": b"\x00" * 20,
            "value": 100,
            "data": { "foo": "bar" }
        }

        return data

    def make_transaction(self, sender_privkey=None, tx_data=None):
        if sender_privkey is None:
            sender_privkey = self.default_sender_privkey

        if tx_data is None:
            tx_data = self.default_tx_data

        sender_addr = privkey_to_addr(sender_privkey)
        tx_data["nonce"] = self.local_state.get_account(sender_addr).data["nonce"]
        tx = Transaction(tx_data=tx_data).sign(sender_privkey)

        # Apply transaction to the head state directly

        self.local_state.apply_transaction(tx)

        # Append the new transaction to block without broadcasting on p2p network
        self.block.transactions.append(tx)

        return tx

    def make_candidate_block(self):
        # 1. Get basic block info
        # 2. Collect transactions
        # 3. Calculate roots
        # 4. Mark the block as a candidate
        self.block.make_roots(self.local_state)
        return self.block
