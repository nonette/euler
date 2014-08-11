## Find the sum of even Fibonacci numbers below 4*10**6
#
# There are only 11 such numbers.

import logging

logger = logging.getLogger(__name__)

def p002(N=4*10**6):
    a,b,c = 1,1,2
    ret_val = 0
    while c < N:
        ret_val += c
        a,b,c = b+c,b+2*c,2*b+3*c
        logger.debug(c)
    return ret_val
