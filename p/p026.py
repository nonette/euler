## Find d<1000 for which the decimal fraction of 1/d contains the longest recurring cycle
#
# A little sloppy... thinks terminating fractions end in 0 repeating

import logging

import lib.numty as numty

logger = logging.getLogger(__name__)

def cycle(d):
    l = []
    n = 1
    seen_n = {}
    while n not in seen_n:
        seen_n[n] = len(l)
        l.append(n/d)
        n = (n%d)*10
    logger.debug(l[seen_n[n]:])
    return len(l)-seen_n[n]

def p026():
    return max((cycle(d), d) for d in range(1,1000))[1]

