## Find the sum of the digits in 100!

import utils

def p020(N=100):
    return sum(int(d) for d in str(utils.prod(range(1,N+1))))
