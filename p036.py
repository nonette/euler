## Find all numbers less than 10**6 which are palindromes in both base 10 and
# base 2
#

import logging

logger = logging.getLogger(__name__)

def p036(N=10**6):
    acc = 0
    for n in range(N):
        if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]:
            logger.debug(n)
            acc += n
    return acc
