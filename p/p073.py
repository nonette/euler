## Find the number of simple fractions strictly between 1/3 and 1/2 with
#  with denominator le 12000
#
# observe gcd(n,d) = gcd(d-n,d)
# this is not very fast

import p069
import lib.numty as numty

def p073(N=12000):
    retval = 0
    for d in range(2,N+1):
        total = p069.phi(d)
        lowerthird = len([n for n in range(d/3+1) if numty.gcd(n,d) == 1])
        retval += total/2-lowerthird
    return retval


