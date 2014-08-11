## Calculate sum phi(n) for n in range(1,10**6+1)

import utils
import p069

def p072(N=10**6):
    table = utils.factortable(N+1)
    return sum(p069.phi(n, table[n]) for n in range(2,N+1))

