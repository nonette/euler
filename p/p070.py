## Find n < 10**7 for which phi(n) is a permutation of n and the ratio n/phi(n)
# is minimized
#
# Guess that n=p*q
# this is supersketch

import lib.numty as numty

def p070():
    primes = numty.sieve(10**4)
    best = (1000,0)
    for i,p in enumerate(primes):
        if p < 1000:
            continue
        for q in primes[i-1::-1]:
            n = p*q
            if n > 10**7:
                continue
            phi = (p-1)*(q-1)
            if sorted(str(phi)) == sorted(str(n)):
                cand = (1.0*n/phi, n)
                if cand < best:
                    best = cand
    return best[1]
