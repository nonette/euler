# Find the sum of all primes below 2*10**6

import utils

def p010(N=2*10**6):
    return sum(utils.sieve(2*10**6))
