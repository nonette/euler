## Find the first four consecutive integers which each have four distinct prime
# factors
#
# really cheating with the upper bound here

import lib.numty as numty

def p047(N=4, lim=150000):
    table = [len(x.keys()) for x in numty.factortable(lim)]
    for n in range(len(table)):
        if all(table[n+i]>=N for i in range(N)):
            return n
    return p047(N, 10*lim)
