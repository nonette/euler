# find the last ten digits of 28433*2**7830457+1

import lib.numty as numty

def p097():
    return int((28433*numty.pow_mod(2,7830457, 10**10)+1) % 10**10)
