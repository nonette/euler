# Find the sum of all primes below 2*10**6

import lib.numty as numty

def p010(N=2*10**6):
    return sum(numty.sieve(2*10**6))
