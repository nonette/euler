## Find the prime below 10**6 which can be written as the longest sum of
# consecutive prime numbers
#
# Totally dominated by calculating the table of primes... getting fiddly with
# the limit
#
# Solution: 

import logging

import lib.numty as numty

logger = logging.getLogger(__name__)

def p050(N=10**6, lim = 4000):
    primes = numty.sieve(lim)
    primeset = set(primes)
    bestprime = 0
    bestlen = 0
    bestbase = 0
    i = 0
    while True:
        if i+bestlen > len(primes):
            logger.error('Limit was too low!')
            return
        cand = sum(primes[i:i+bestlen])
        if cand >= N:
            break
        j = i+bestlen
        while cand < N:
            if j >= len(primes):
                logger.error('Limit was too low!')
                return
            cand += primes[j]
            j += 1
        while j > i+bestlen:
            if numty.isprime(cand):
                bestprime = cand
                bestlen = j-i
                bestbase = primes[i]
                break
            cand -= primes[j-1]
            j -= 1
        i += 1
    logger.debug((bestlen, primes[bestbase:bestbase+bestlen]))
    return bestprime
