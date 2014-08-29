## Find the sum of the digits in 100!

import lib.numty as numty

def p020(N=100):
    return sum(int(d) for d in str(numty.prod(range(1,N+1))))
