## Find the numerator of the max fraction less than 3/7 with denominator bounded
#  by 10**6
#

from fractions import Fraction

def p071(N=10**6):
    bestval, best = 1, 0
    for n in range(1,N+1):
        if n % 7 == 0:
            continue
        x = 3*n/7
        cand = Fraction(x,n)
        val = Fraction(3,7)-Fraction(x,n)
        if val < bestval:
            bestval = val
            best = cand
    return best.numerator
        

