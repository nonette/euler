## Find the sum of all 0..9 pandigital numbers such that
# The substring d[k:k+2] is divisible by the kth prime
#
# Solution: 16695334890

from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

def p043():
    primes = [1,2,3,5,7,11,13,17]
    extendmap = {}
    for p in primes:
        multp = [str(n*p).zfill(3) for n in range(1,1000/p)]
        multp = [mult for mult in multp if len(set(mult)) == 3]
        pmap = defaultdict(list)
        for mult in multp:
            pmap[mult[1:]].append(mult[0])
        extendmap[p] = pmap
    pandigitals = multp
    for p in primes[-2::-1]:
        newpandigitals = []
        for pandigital in pandigitals:
            key = pandigital[:2]
            for extension in extendmap[p][key]:
                if extension not in pandigital:
                    newpandigitals.append(extension+pandigital)
        pandigitals = newpandigitals
    logger.debug(pandigitals)
    return sum(int(pandigital) for pandigital in pandigitals)

