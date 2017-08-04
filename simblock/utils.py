from Crypto.Hash import keccak
from py_ecc.secp256k1 import privtopub, ecdsa_raw_sign
# import pickle
# import marshal
import json
from collections import OrderedDict
from copy import deepcopy

def sha3_256(data):
    if isinstance(data, str):
        d = bytes(data, "utf-8")
    else:
        d = bytes(data)

    return keccak.new(digest_bits=256, data=d).digest()

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

def copy(data):
    return deepcopy(data)

# Use serializer to encode instead of RLP
def simple_encode(data):
    data = copy(data)

    def bytes_to_str(b):
        if isinstance(b, bytes):
            b = int.from_bytes(b, byteorder='big')
        return b

    def nested_encode(d):
        try:
            if len(list(filter(lambda e: isinstance(e, dict), d.values()))) > 0:
                return dict(sort_dict({ bytes_to_str(k): nested_encode(d[k]) for k in d.keys() }))
            else:
                return dict(sort_dict({ bytes_to_str(k): bytes_to_str(d[k]) for k in d.keys() }))
        except AttributeError as e:
            if isinstance(d, list):
                return [nested_encode(t) for t in d]
            else:
                return bytes_to_str(d)

    data = nested_encode(data)
    return json.dumps(data)

def simple_decode(data):
    return json.loads(data)

def sort_dict(data):
    return dict(OrderedDict(sorted(data.items(), key=lambda t: t[0])))
