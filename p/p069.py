## Find n le 10**6 for which n/phi(n) is maximized

import lib.numty as numty

def phi(n, factoredn=None):
    if not factoredn:
        factoredn = numty.factor(n)
    return numty.prod(p**(e-1)*(p-1) for p,e in factoredn.items())

def p069(N=10**6):
    table = numty.factortable(N+1)
    best = max((1.0*n/phi(n, table[n]), n) for n in range(N+1))
    return best[1]


