## Find the perimeter p <= 1000 corresponding to the most integral length right 
# triangles 
#
# Every Pythagorean triple is uniquely specified by (k,m,n) with (m,n)=1
# and one of m,n even
# giving k(2mn, m**2-n**2, m**2+n**2)
# with perimeter 2km(m+n) -- require m+n < 2*m so that n < m
#
# For a given factorization, we must choose to distribute the odd prime factors
# between k and one of m, m+n. For the powers of 2, k
# cannot get all of them....
# I can definitely estimate this as the number with the most factors, but it's
# not exact. Observe 840 = 7*5!
#
# Solution: 840

import logging
import utils

def triangle(k,m,n):
    m,n = max(m,n), min(m,n)
    return sorted((2*m*n*k, k*(m**2-n**2), k*(m**2+n**2)))

def pythcount(perimeter):
    acc = 0
    for a in range(1, perimeter/2):
        for b in range(1, a+1):
            c = perimeter-a-b
            if c <= a:
                break
            if a**2 + b**2 == c**2:
                logging.debug('%d %d %d' % (a,b,c))
                acc += 1
    return acc    

def p039(N=1000):
    # a little microoptimization
    # starting at 12, the perimeter of the smallest integral right triangle
    # going up by 4 since we need the leading 2 and one of m,n to be even
    return max((pythcount(p), p) for p in range(12,N+1,4))[1]


