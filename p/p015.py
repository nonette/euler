## Calculate choose(40,20)

from fractions import Fraction

import lib.numty as numty

def choose(n,k):
    return int(numty.prod(Fraction(n-i,k-i) for i in range(k)))

def p015(N=20):
    return choose(2*N, N)
