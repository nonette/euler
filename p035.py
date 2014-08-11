## How many circular primes are there below 10**6?

import logging

import utils

logger = logging.getLogger(__name__)

def p035(N=10**6):
    primes = utils.sieve(N)
    primeset = set(primes)
    count = 0
    for p in primes:
        str_p = str(p)
        if all(int(str_p[n:]+str_p[:n]) in primeset for n in range(len(str_p))):
            logger.debug(p)
            count += 1
    return count

