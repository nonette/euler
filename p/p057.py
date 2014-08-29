## Count the continued fraction representations of sqrt(2) with more digits in
# numerator than the denominator

from fractions import Fraction
import logging

logger = logging.getLogger(__name__)

def p057(N=1000):
    counter = 0
    f = Fraction(3,2)
    for n in range(N):
        logger.debug(f)
        if len(str(f.numerator)) > len(str(f.denominator)):
            counter += 1
        f = 1 + 1/(1+f)
    return counter
