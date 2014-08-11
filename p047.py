## Find the first four consecutive integers which each have four distinct prime
# factors
#
# really cheating with the upper bound here

import utils

def p047(N=4, lim=150000):
    table = [len(x.keys()) for x in utils.factortable(lim)]
    for n in range(len(table)):
        if all(table[n+i]>=N for i in range(N)):
            return n
    return p047(N, 10*lim)
