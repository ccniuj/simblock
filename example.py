from simblock.tools.api import API

api = API()
api.make_transaction()
api.make_transaction()
api.make_transaction()
block = api.make_candidate_block()
n = block.mine()
print(n)
