## Find the sum of the digits in the numerator of the 100th convergent of e
# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, etc]
# 2 1
# 1 0

import logging

def e():
    yield 2
    yield 1
    n = 1
    while True:
        yield 2*n
        yield 1
        yield 1
        n += 1

def p065(N=100):
    cf = e()
    num2,den2 = 0,1
    num1,den1 = 1,0
    for n in range(N):
        a = cf.next()
        num2,den2,num1,den1 = num1,den1,a*num1+num2,a*den1+den2
        logging.debug('%d %d' % (num1, den1))
    return sum(int(d) for d in str(num1))

