# Find the sum of the perimeters of all almost-equal-equilateral triangles with
# integral side lengths and area, whose perimeters do not exceed 10**9
#
# If our sides are a,a,a pm 1, the area is
# (a pm 1)/4 * sqrt((3a pm 1)*(a mp 1))
#
# The repeated side needs to be odd. Can we say more?

import math
from multiprocessing import Pool

def heron(a,b,c):
    return math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/4

def checkrange(r):
    lb, ub = r
    acc = []
    for k in range(lb,ub):
        x = k*(3*k+2)
        if int(math.sqrt(x))**2 == x:
            acc.append((2*k+1, 2*k+1, 2*k+2))
            #print acc[-1]
        y = (3*k+1)*(k+1)
        if int(math.sqrt(y))**2 == y:
            acc.append((2*k+1, 2*k+1, 2*k))
            #print acc[-1]
        k += 1
    return acc

def p094(N=10**9):
    return sum(sum(checkrange((1,N/6)),()))

def parallel(N=10**9, k=4):
    lim = N/6
    p = Pool(k)
    result = p.map(checkrange, [((i*(lim/k)+1, (i+1)*(lim/k))) for i in range(k)])
    return sum(sum(sum(result,[]),()))
