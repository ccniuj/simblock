from simblock.tools.api import API

api = API()
print("Chain Block hash:", api.chain.head.header.hash)
print("Chain Block header:\n", dict(api.chain.head.header))

for _ in range(100):
    api.make_transaction()
    api.make_transaction()
    api.make_transaction()
    api.mine()
    print("\n")
    print("#"*100)
    print("\n")
    print("Chain Block hash:", api.chain.head.header.hash)
    print("Chain Block header:\n", dict(api.chain.head.header))
    print("State root hash:\n", api.chain.state.root_hash)
