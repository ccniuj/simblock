from .utils import privkey_to_addr, sha3_256, ec_sign, simple_encode

class Transaction():
    fields = [
        "nonce",
        "to",
        "value",
        "data",
        "v",
        "r",
        "s",
    ]

    def __init__(self, tx_data=None):
        if tx_data is None:
            raise ValueError("Argument 'tx_data' is not provided.")

        self.tx_data = tx_data
        self.sender = None

        # Signature
        self.v = 0
        self.r = 0
        self.s = 0
        self.signed = False

    def sign(self, privkey):
        if self.signed == True:
            return None
        else:
            raw_hash = sha3_256(simple_encode(dict(self)))
            self.v, self.r, self.s = ec_sign(raw_hash, privkey)
            self.signed = True

        # Set sender
        self.sender = privkey_to_addr(privkey)

        return self

    def __iter__(self):
        return iter([
            ("tx_data", self.tx_data),
            ("sender", self.sender),
            ("v", self.v),
            ("r", self.r),
            ("s", self.s),
            ("signed", self.signed)
        ])
