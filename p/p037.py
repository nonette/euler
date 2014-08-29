## Find the sum of the 11 primes that are truncatable both left and right
#
# primes, aside from 2 and 5, only end in 1,3,7, or 9.

import logging

import lib.numty as numty

logger = logging.getLogger(__name__)

def truncatable(prime):
    str_p = str(prime)
    for n in range(len(str_p)):
        if not numty.isprime(int(str_p[n:])):
            return False
    return True

def p037():
    primes = [2,3,5,7]
    allprimes = []
    while primes:
        logger.debug(primes)
        newprimes = []
        for prime in primes:
            for d in [1,3,7,9]:
                if numty.isprime(10*prime+d):
                    newprimes.append(10*prime+d)
        primes = newprimes
        allprimes += primes
    acc = 0
    count = 0
    for prime in allprimes:
        if truncatable(prime):
            logger.debug(prime)
            count += 1
            acc += prime
    logger.debug(count)
    return acc

