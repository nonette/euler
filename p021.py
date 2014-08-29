## Find the sum of all amicable numbers under 10**4
#
# Two numbers are amicable if the sum of the proper divisors of one equals the other
# and vice versa
#
# if n = prod p**e
# then sumdivs(n) = prod (p**(e+1)-1)/(p-1)
# we then subtract out the number itself
#
# Solution: 31626

import logging

import utils

logger = logging.getLogger(__name__)

def p021(N=10**4):
    table = [utils.sigma(f)-n for (n,f) in enumerate(utils.factortable(N))]
    acc = 0
    for n in range(1,N):
        if 0 < table[n] < N and table[table[n]] == n and table[n] != n:
            logger.debug('%d %d' % (n, table[n]))
            acc += n
    return acc

