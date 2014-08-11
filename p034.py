## Find the sum of all numbers which are equal to the sum of the factorials of
# their digits
#
# How to bound this?
# We don't need to check over 2! + 5*8! if only using digits 1..8.
# 9 is tricky because it's so big.
# The answer will need to be at least 6 digits long.
# If there is only one 9, we only need to check between 9! and 9!+5*8!
# If there are two 9s, 2*9! to 2*9!+4*8!
# A couple million things to check?

import logging

import utils

logger = logging.getLogger(__name__)

fact = [utils.prod(range(1,n+1)) for n in range(10)]

def p034():
    acc = 0
    ranges = [(10, fact[2] + 5 * fact[8])]
    for n in range(1,7):
        lower = n*fact[9]
        upper = lower + fact[8]*(len(str(lower))-n)
        ranges.append((lower, upper))
    for l, u in ranges:
        for n in range(l, u):
            if sum(fact[int(d)] for d in str(n)) == n:
                acc += n
                logger.debug(n)
            n += 1
    return acc
