## find the number of n-digit positive integers which are also an nth power
#
# we want n-1 <= lg_10 b^n < n
# so b < 10, game is over when (n-1)/n > lg_10 b

import logging

def p063():
    counter = 0
    for b in range(1,10):
        n = 1
        while True:
            if len(str(b**n)) == n:
                counter += 1
                logging.debug('%d^%d=%d' % (b,n,b**n))
            if len(str(b**n)) < n-1:
                break
            n += 1
    return counter
