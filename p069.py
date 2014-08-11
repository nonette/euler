## Find n le 10**6 for which n/phi(n) is maximized

import utils

def phi(n, factoredn=None):
    if not factoredn:
        factoredn = utils.factor(n)
    return utils.prod(p**(e-1)*(p-1) for p,e in factoredn.items())

def p069(N=10**6):
    table = utils.factortable(N+1)
    best = max((1.0*n/phi(n, table[n]), n) for n in range(N+1))
    return best[1]


