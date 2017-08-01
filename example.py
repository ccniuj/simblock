from simblock.tools import tester

t = tester.TestApp()
t.make_transaction()
t.make_transaction()
t.make_transaction()
block = t.make_candidate_block()
