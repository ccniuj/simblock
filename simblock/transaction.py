from simblock import utils

class Transaction():
    """
    A simple implementation of transaction referencing Ethereum's.
    """

    def __init__(self, nounce, to, value, v=0, r=0, s=0):
        # fields = [
        #     ("nounce", ""),
        #     ("to", ""),
        #     ("value", ""),
        #     ("v", ""),
        #     ("r", ""),
        #     ("s", "")
        # ]
        to = utils.normalize_address(to)

