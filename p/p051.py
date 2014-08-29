## Find the smallest prime which is part of an eight prime mask family
#
# There are 62 nontrivial masks on six digits
# Don't allow leading zeroes or the answer will be 000109

import logging

import lib.numty as numty

logger = logging.getLogger(__name__)

def p051(N=6,target=8):
    primes = numty.sieve(10**N)
    primes = [str(p) for p in primes if len(str(p)) == N]
    primeset = set(primes)
    masks = [bin(x)[2:].zfill(N)  for x in range(1,2**N-1)]
    for prime in primes:
        for mask in masks:
            if len(set(''.join(b for a,b in zip(mask,prime) if a=='0'))) == 1:
                family = [''.join((b if a == '1' else str(i)) for a,b in zip(mask, prime)) for i in range(10)]
                family = [p for p in family if p in primeset]
                if len(family) == target:
                    logger.debug(family)
                    return prime
