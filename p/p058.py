## Find N s.t. the ratio of primes along both diagonals of the spiral falls below 10%
#
# The diagonals are (2*n-1)**2, (2*n-1)**2+2*n, (2*n-1)**2+4*n, (2*n-1)**2+6*n,

import lib.numty as numty

def p058(target=0.1):
    primecount = 0
    n = 1
    while True:
        corners = [(2*n-1)**2+2*n, (2*n-1)**2+4*n, (2*n-1)**2+6*n]
        primecount += sum(1 for corner in corners if numty.isprime(corner))
        if 1.0*primecount/(4*n+1) < target:
            return 2*n+1
        n += 1
