# Largest prime factor

import lib.numty as numty

def p003(N=600851475143):
        return max(numty.factor(N).keys())
