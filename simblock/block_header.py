import pickle
from .utils import sha3_256

empty_data = {
    "prevhash": "",
    "difficulty": 0,
    "timestamp": 0,
    "nonce": ""
}

_genesis_data = {
    "prevhash": b"\x00" * 32,
    "difficulty": 131072,
    "timestamp": 0,
    "nonce": ""
}

class BlockHeader():
    fields = [
        "prevhash",
        "difficulty",
        "number",
        "timestamp",
        "nonce",
        "state_root",
        "transaction_root"
    ]

    def __init__(self, data=None):
        if data is None:
            data = empty_data

        self.prevhash = data["prevhash"]
        self.difficulty = data["difficulty"]
        self.timestamp = data["timestamp"]
        self.nonce = data["nonce"]

    @property
    def hash(self):
        return sha3_256(pickle.dumps(self))

GENESIS_BLOCK_HEADER = BlockHeader(data=_genesis_data)
