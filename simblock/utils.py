from Crypto.Hash import keccak

def sha3_256(data):
    return keccak.new(digest_bits=256, data=bytes(data)).digest()

def privkey_to_addr(key):
    return sha3_256(key)
