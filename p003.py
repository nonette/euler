# Largest prime factor

import utils

def p003(N=600851475143):
    return max(utils.factor(N).keys())
