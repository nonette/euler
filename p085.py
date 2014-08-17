# Find the area of the grid containing closest to 2*10**6 rectangles
#
# The number of rectangles in an mxn grid is
# choose(m+1,2)*choose(n+1,2)
#
# invert n**2+n-2k=0
# n = -1+sqrt(1+8k)/2

import math

from p015 import choose

def p085():
    target = 2*10**6
    bestm, bestn, best_val = -1,-1,-1
    for m in range (1,2000):
        k = target/choose(m+1,2)
        n = int(round((math.sqrt(1+8*k)-1)/2))
        approx = choose(m+1,2)*choose(n+1,2)
        val = abs(approx-target)
        if best_val == -1 or val < best_val:
            bestm, bestn, best_val = m, n, val
    return bestm*bestn         
