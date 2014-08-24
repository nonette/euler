import logging
import math
import operator
import random

logger = logging.getLogger(__name__)

def drawgrid(N):
    print ('   '.join('|'*(N+1))+'\n').join('---'.join('+'*(N+1))+'\n' for n in range(N+1))

def fact(N):
    return prod(range(1,N+1))

def prod(r):
    return reduce(operator.mul, r, 1)

def pow_mod(b, e, n):
    if e == 0:
        return 1
    return (pow_mod(b**2 % n, e/2, n) * b**(e%2)) % n

def isprime(n, userand=False, rounds=5):
    """Miller-Rabin primality test"""
    bases = [2,3,5,7,11]
    if n in bases:
        return True
    if n % 2 == 0 or n == 1:
        return False

    LIMIT = 2152302898747
    if not userand and n >= LIMIT:
        logger.warning("%d larger than guaranteed range" % n)
    if userand:
        bases = [random.randrange(2,n) for i in range(rounds)]

    # write n = 2**s * d + 1
    d = n-1
    s = 0
    while d % 2 == 0:
        s += 1
        d /= 2
    
    # look for a nontrivial sqrt(1) of the form base**(2**r * d)
    for base in bases:
        x = pow_mod(base, d, n)
        # x trivial
        if x in (1,n-1):
            continue
        for r in range(1,s):
            x = x**2 % n
            # previous x was nontrivial!
            if x == 1:
                return False
            # x is trivial, inconclusive
            if x == n-1:
                break
        else:
            # current x is nontrivial or Fermat is failing
            return False
    # probably prime (definitely prime if LIMIT guarantee applies)
    return True
        


def sieve(N):
    """Sieve of Erastothenes for n <= N"""
    table = range(N+1)
    table[1] = 0
    for i in table:
        if i == 0:
            continue
        k = 2*i
        while k < N+1:
            table[k] = 0
            k += i
    return [i for i in table if i != 0]

def firstnprimes(N):
    shortlist = [2,3,5,7,11]
    if N <= len(shortlist):
        return shortlist[:N]
    # from Wiki:Prime_counting_function#Inequalities
    upperbound = int(N*(math.log(N)+math.log(math.log(N))))+1
    return sieve(upperbound)[:N]

def factor(n):
    """Brute force factor.
    Returns dictionary {p:e} mapping prime factors to their multiplicity."""
    ret_val = {}
    if n == 0:
        return ret_val
    p = 2
    while True:
        if n%p == 0:
            n /= p
            e = 1
            while n%p == 0:
                e += 1
                n /= p
            ret_val[p] = e
        if n == 1:
            return ret_val
        p+=1

def factortable(N):
    """Sieve based factor.
    Return list of dictionaries {p:e} mapping prime factors to their
    multiplicity for n <= N."""
    table = range(N+1)
    table[1] = 0
    factors_table = [{} for n in range(N+1)]
    for i in table:
        if i == 0:
            continue
        factors_table[i][i] = 1
        multiple_of_i = 2*i
        while multiple_of_i < N+1:
            table[multiple_of_i] = 0
            e = 1
            tmp = multiple_of_i/i
            while tmp % i == 0:
                e += 1
                tmp /= i
            factors_table[multiple_of_i][i] = e
            multiple_of_i += i
    return factors_table

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a       

