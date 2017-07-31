class Block():
    def __init__(self, header=None, transactions=None):
        if not header:
            raise ValueError("Argument 'header' is not provided.")
        self.header = header
        self.transactions = transactions or []

    def from_prevstate(self, state=None, timestamp=None):
        if not state:
            raise ValueError("Argument 'state' is not provided.")

        prev_header = state.prev_headers[0]
        next_header = {
            "prevhash": prev_header.hash,
            "timestamp": timestamp or prev_header.timestamp + 1,
            "difficulty": prev_header.difficulty,
            "nonce": ""
        }

        self.header.prevhash = next_header["prevhash"]
        self.header.timestamp = next_header["timestamp"]
        self.header.difficulty = next_header["difficulty"]
        self.header.nonce = next_header["nonce"]

        return self
