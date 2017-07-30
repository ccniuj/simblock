import pickle
from .utils import sha3_256

class BlockHeader():
    fields = [
        "prevhash",
        "state_root",
        "tx_root",
        "difficulty",
        "number",
        "timestamp",
        "nonce"
    ]

    def __init__(self, data=None):
        self.data = data

    @property
    def hash(self):
        return sha3_256(pickle.dumps(self))

_genesis_data = {
    "prevhash": b"\x00" * 32,
    "difficulty": 131072,
    "timestamp": 0,
    "nonce": ""
}

GENESIS_BLOCK_HEADER = BlockHeader(data=_genesis_data)
