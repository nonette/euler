# How many perimeters <= 15*10**5 allow exactly one integer sided right
#  triangle?
#
#  k(m**2-n**2,2mn,m**2+n**2) where (m,n)=1, m+n odd
#  p = 2km(m+n) <= N
#  m+n <= sqrt(N/k)
#
#  36 = 2*3*2*3
#  108 = 2*3*12*9

import math

import lib.numty as numty

def uniques(N):
    table = [[] for n in range(N+1)]
    for k in range(1,N/12+1):
        for mplusn in range(3,int(math.sqrt(N/k))+1,2):
            for m in range(mplusn/2+1, mplusn):
                p = 2*k*m*mplusn
                if p > N:
                    break
                if numty.gcd(m,mplusn) != 1:
                    continue
                table[p].append((k,mplusn-m,m))

    return [p for p in range(len(table)) if len(table[p]) == 1]

def p075(N=15*10**5):
    return len(uniques(N))

