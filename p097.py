# find the last ten digits of 28433*2**7830457+1

import utils

def p097():
    return int((28433*utils.pow_mod(2,7830457, 10**10)+1) % 10**10)
