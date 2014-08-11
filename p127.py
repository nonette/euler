## Find sum c over all positive triples a,b,c s.t. 
#  (a,b) = 1, a<b, a+b=c, rad(abc) < c, and c < 120000
#
# It's necessary that
# rad(abc) = rad(a)rad(b)rad(a+b) < a+b
# rad(a) < c/rad(c)
#
# Solution: 18407904

import logging

import utils

logger = logging.getLogger(__name__)

def rad(n):
    return utils.prod(utils.factor(n).keys())

def radtable(n):
    return [utils.prod(r.keys()) for r in utils.factortable(n)]

def p127(N = 120000):
    rad_table = radtable(N)
    a_table = sorted([(rad_table[a], a) for a in xrange(1,N)])
    acc = 0

    for c in xrange(N):
        lim = c/rad_table[c]
        for rad_a, a in a_table:
            if rad_a > lim:
                break
            if a >= (c+1)/2:
                continue
            if utils.gcd(rad_table[a],rad_table[c]) == 1:
                if rad_table[a]*rad_table[c-a]*rad_table[c] < c:    
                    logger.debug('%d %d %d' % (a, c-a, c))
                    acc += c
    return acc
