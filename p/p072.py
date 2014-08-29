## Calculate sum phi(n) for n in range(1,10**6+1)

import lib.numty as numty
import p069

def p072(N=10**6):
    table = numty.factortable(N+1)
    return sum(p069.phi(n, table[n]) for n in range(2,N+1))

