## Find the sum of all numbers which can be written as a pandigital product
#
# 2-3 or 1-4 split. About 10000 possibilities, let's just run them all.

import itertools
import logging

logger = logging.getLogger(__name__)

def check(str1, str2):
    product = int(str1)*int(str2)
    s = str1+str2+str(product)
    if len(s) == 9 and set(s) == set('123456789'):
        logger.debug('%s * %s = %d' % (str1, str2, product))
        return product
    return 0

def p032():
    acc = set([])
    for digits in itertools.permutations('123456789', 5):
        digits = ''.join(digits)
        acc.add(check(digits[:1], digits[1:]))
        acc.add(check(digits[:2], digits[2:]))
    return sum(acc)
