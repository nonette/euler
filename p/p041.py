## Find the largest n-digit pandigital prime.
# Only defined up to n=9. n=9 doesn't work because it'll be divisible by 9.
# Let's start with 8.
#
# Solution: 7652413

import itertools

import lib.numty as numty

def p041():
    for N in range(8,0,-1):
        for p in itertools.permutations(range(N,0,-1)):
            n = sum(d*10**(len(p)-1-i) for (i,d) in enumerate(p))
            if numty.isprime(n):
                return n
