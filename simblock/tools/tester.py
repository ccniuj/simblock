from simblock.utils import sha3_256, privkey_to_addr
from simblock.state import State
from simblock.env import Env
from simblock.chain import Chain

class TestApp():
    def __init__(self):
        env = Env()
        alloc = self.make_alloc()
        state = State(env=env).from_alloc(alloc)
        chain = Chain(state=state, env=env)
        self.chain = chain

    def make_alloc(self):
        keys = [sha3_256(i) for i in range(1, 10)]
        addrs = [privkey_to_addr(key) for key in keys]
        alloc = { addr: { "balance": 10**24, "nonce": 123 } for addr in addrs }
        return alloc
