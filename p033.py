## Find the product of the four nontrivial curious fractions with 2 digits in
# the numerator and denominator
# ab/ac, ab/ca, ab/bc, ab/cb

from fractions import Fraction
import logging

import utils

logger = logging.getLogger(__name__)

def check(a, b, c, d):
    if c >= d:
        return 1
    if Fraction(a,b) == Fraction(c,d):
        logger.debug('%d/%d = %d/%d' % (a,b,c,d))
        return Fraction(a,b)
    return 1


def p033():
    acc = set([])
    for a in range(1,10):
        for b in range(1, 10):
            for c in range(1, 10):
                ab = 10*a+b
                ac = 10*a+c
                ca = 10*c+a
                bc = 10*b+c
                cb = 10*c+b
                acc.add(check(ab, ac, b, c))
                acc.add(check(ab, ca, b, c))
                acc.add(check(ab, bc, a, c))
                acc.add(check(ab, cb, a, c))
    product = utils.prod(acc)
    return product.denominator

