## Find chains starting below 10**6 containing exactly 60 nonrepeating terms
#
# Every chain ends in a 1-loop or one of the three known longer loops.

import logging

import lib.numty as numty

def magic(n):
    return sum(numty.prod(range(1,int(d)+1)) for d in str(n))

table = {145:1, 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}

def magiclen(n):
    if n not in table:
        nextn = magic(n)
        if nextn == n:
            table[n] = 1
        else:
            table[n] = magiclen(nextn)+1
    return table[n]

def p074():
    count = 0
    for n in range(1,10**6+1):
        if magiclen(n) == 60:
            count += 1
        if magiclen(n) == 60 or magiclen(n) == 1:
            logging.debug('%d %d' % (n, magiclen(n)))
    return count
