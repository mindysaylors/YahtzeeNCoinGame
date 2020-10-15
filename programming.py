"""
Author: Mindy Saylors
EE209AS Fall 2020
Prof: Ankur Mehta
Problem Set 0
Problem 4
"""

import numpy
import matplotlib.pyplot as plt
import enum

class CoinResult(enum.Enum):
    HEADS = enum.auto()
    TAILS = enum.auto()

    def __str__(self):
        return self.name[0]

    def __repr__(self):
        return self.name[0]

class Coin:
    def __init__(self, p_heads):
        self.p_heads = p_heads

    @property
    def p_tails(self):
        return 1 - self.p_heads

    def __call__(self):
        # Okay, this *could* lead to bias, but it wont. Plus, rand() returns
        # from [0, 1), so this compensates the upper range for the 1 they are
        # missing.
        if numpy.random.rand() >= self.p_heads:
            return CoinResult.TAILS
        return CoinResult.HEADS

def policyFct(states):
    """ Determine the current policy.

    We are trying to get all tails, so lets check which are heads

    Parameters
    ----------
    states : list of states
        The current state of each flip

    Returns
    -------
    list
        The number of coins to flip. True == flip, False == no flip.
    """
    return [state == CoinResult.HEADS for state in states]

if __name__ == "__main__":
    nFlips = 2
    coins = [Coin(0.5) for _ in range(3)]
    states = [coin() for coin in coins]
    for _ in range(nFlips):
        print("S: {}".format(states))
        policies = policyFct(states)
        print("Actions: {}".format(policies))
        for idx, policy in enumerate(policies):
            if policy:
                states[idx] = coins[idx]()
    print("S: {}".format(states))



