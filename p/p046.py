## Find the smallest odd composite number that cannot be written as the sum of a
# prime and twice a square
#
# limit chosen by observation. could run it for increasing limit until an answer
# is found?

import math

import lib.numty as numty

def p046():
    lim = 10**4
    primes = numty.sieve(lim)
    table = [1,0]*(lim/2)
    table[1] = 1
    for n in range(int(math.sqrt(lim/2))):
        i = 2*n**2
        for p in primes:
            if p+i > lim:
                break
            table[p+i] = 1
    return table.index(0)
