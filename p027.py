## Find ab which produces the maximum stretch of primes starting with n=0
# |a|, |b| < 1000
# n**2 + an + b
#
# b needs to be a prime number
# a can't be smaller than -b+1
# caching the primes is about 10x speed improvement

import utils

def p027(N = 10**3):
    lim = 10*N
    table = set(utils.sieve(lim))
    primes = utils.sieve(2*N+1)

    best = 0
    best_ab = (0,0)

    for b in primes:
        if b > N:
            break
        for c in primes:
            a = c - b - 1
            if a > N:
                break
            count = 2
            while True:
                cand = count**2+a*count+b
                if cand < 0:
                    break
                if cand < lim and cand not in table:
                    break
                if cand >= lim and not utils.isprime(cand):
                    break
                count += 1
            if count > best:
                best_ab = (a,b)
                best = count
    return best_ab[0]*best_ab[1]
