## Find sum(n**n for n in range(1,1001)) mod 10**10
#
# Slower to call pow_mod.
#

import lib.numty as numty

def p048(N=1000):
    return sum(n**n for n in range(1,N+1)) % 10**10
