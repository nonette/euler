## Find the least common multiple of the numbers 1..20
#

import utils

def p005(N=20):
    primes = utils.sieve(N)
    ret_val = 1
    for p in primes:
        tmp = p
        while tmp <= N:
            tmp *= p
            ret_val *= p
    return ret_val

def lcm(a,b):
    return a*b/utils.gcd(a,b)

def lcm_sol(N=20):
    return reduce(lcm, range(1,N+1), 1)
