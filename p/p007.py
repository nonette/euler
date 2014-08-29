## Find the 10001st prime

import lib.numty as numty

def p007(N=10001):
    return numty.firstnprimes(N)[-1]
