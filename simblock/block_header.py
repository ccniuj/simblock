from .utils import sha3_256, simple_encode

empty_data = {
    "number": 0,
    "prevhash": "",
    "difficulty": 13000,
    "timestamp": 0,
    "nonce": ""
}

_genesis_data = {
    "number": 0,
    "prevhash": b"\x00" * 32,
    "difficulty": 13000,
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

        self.number = data["number"]
        self.prevhash = data["prevhash"]
        self.difficulty = data["difficulty"]
        self.timestamp = data["timestamp"]
        self.nonce = data["nonce"]

        # roots
        self.state_root = None
        self.tx_root = None

    @property
    def hash(self):
        return sha3_256(simple_encode(dict(self)))

    def __iter__(self):
        return iter([
            ("number", self.number),
            ("prevhash", self.prevhash),
            ("difficulty", self.difficulty),
            ("timestamp", self.timestamp),
            ("nonce", self.nonce)
        ])

GENESIS_BLOCK_HEADER = BlockHeader(data=_genesis_data)
