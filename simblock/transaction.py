import pickle
from .utils import privkey_to_addr, sha3_256, ec_sign

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
            raw_hash = sha3_256(pickle.dumps(self))
            self.v, self.r, self.s = ec_sign(raw_hash, privkey)
            self.signed = True

        # Set sender
        self.sender = privkey_to_addr(privkey)

        return self
