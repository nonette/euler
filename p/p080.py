# Find the sum of the first 100 digit sums of all the irrational square roots of
# numbers below 100

import math
import decimal

def p080(N=100):
    numdigits = 100
    decimal.getcontext().prec = numdigits+10

    acc = 0
    for n in range(N):
        if int(math.sqrt(n))**2 == n:
            continue
        sqrtn = decimal.Decimal(n).sqrt()
        digitsum = sum(int(d) for d in str(sqrtn)[:numdigits+1] if d in
        '0123456789') # skip the decimal point
        acc += digitsum
    return acc

