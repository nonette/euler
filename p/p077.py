## What is the first number that can be written as the sum of primes in over
#  5000 different ways?

import lib.numty as numty

table = numty.sieve(5000)
cache = {}
def primep(n, i):
    if n == 0:
        return 1
    if i < 0:
        return 0
    p = table[i]
    if (n,p) not in cache:
        cache[(n,p)] = sum(primep(n-p*k, i-1) for k in range(n/p+1))
    return cache[(n,p)]

def primepartitions(n):
    if n > table[-1]:
        raise ValueError("n=%d unexpectedly larger than largest summand %d" % (n, table[-1]))
    return primep(n,n)

def p077():
    for n in range(5000):
        if primepartitions(n) > 5000:
            return n
