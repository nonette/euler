## Find the next largest triangular number that is also pentagonal and hexagonal
# after T[285].
#
# Observe that the hexagonal numbers are every other triangular number.
#
# Solution: 1533776805

import math

from p044 import pent, unpent

def hexagon(n):
    return n*(2*n-1)

def p045(lb=285):
    n = lb+1
    while True:
        k = hexagon(n)
        if pent(unpent(k)) == k:
            return k
        n += 1

