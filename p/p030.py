## Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits
#
# 
# Don't need to check above 300000
# 3**5 + 5*9**5 is already too small

import logging

logger = logging.getLogger(__name__)

def p030(N=5):
    if N <= 5:
        lim = 300000
    else:
        logger.error("Can't handle %d, only N <= 5." % N)
        return
    acc = 0
    for n in range(2,lim):
        if sum(int(d)**N for d in str(n)) == n:
            logger.debug(n)
            acc += n
    return acc
