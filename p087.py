# Find the number of numbers below 5*10**6 which are the sum of a prime square,
# cube, and fourth power
#
# There aren't that many, they can be double-counted. just enumerate.

import bisect
import logging
import math

import utils

def p087(N=5*10**7):
    primes = utils.sieve(int(math.sqrt(N)))
    squares = [p**2 for p in primes if p**2 < N]
    cubes = [p**3 for p in primes if p**3 < N]
    fourthpows = [p**4 for p in primes if p**4 < N]
    goodnums = set(a+b+c for a in squares for b in cubes for c in fourthpows if
            a+b+c < N)
    return len(goodnums)
