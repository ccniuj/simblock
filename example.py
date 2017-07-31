from simblock.tools import tester

t = tester.TestApp()
store = t.head_state.trie.db.store
tx = t.make_transaction()
