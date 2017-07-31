from Crypto.Hash import keccak
from py_ecc.secp256k1 import privtopub, ecdsa_raw_sign

def sha3_256(data):
    return keccak.new(digest_bits=256, data=bytes(data)).digest()

def privkey_to_addr(key):
    key = normalize_key(key)
    x, y = privtopub(key)
    return sha3_256(encode_int32(x) + encode_int32(y))[12:]

def normalize_key(key):
    if len(key) == 32:
        res = key

    return res

def encode_int32(x):
    return x.to_bytes(32, byteorder="big")

def ec_sign(raw_hash, key):
    v, r, s = ecdsa_raw_sign(raw_hash, key)
    return v, r, s
