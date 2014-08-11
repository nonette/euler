## Find the value of D le 10**3 with the largest minimal solution in x to
#  x**2-D*y**2=1

import logging

import p064

def convergents(cf):
    h1,k1 = 1,0
    h2,k2 = cf[0], 1
    yield (h2,k2)
    cf = cf[1:]
    n = 0
    while True:
        a = cf[n]
        h1,k1,h2,k2 = h2,k2,a*h2+h1,a*k2+k1
        yield (h2,k2)
        n = (n+1)%len(cf)

def p066(N=10**3):
    bestd = 0
    bestx = 0
    for n in range(N+1):
        cf = p064.cfsqrt(n)
        if len(cf) == 1:
            continue
        convs = convergents(cf)
        while True:
            x,y = convs.next()
            if x**2-n*y**2 == 1:
                logging.debug('%d**2 - %d*%d**2 == 1' % (x,n,y))
                if x > bestx:
                    bestx = x
                    bestd = n
                break
    return bestd

