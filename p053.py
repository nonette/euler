## Count the number of n,r, n in range(1,101) s.t. choose(n,r) > 10**6
#

import p015

def p053(lim=100, target=10**6):
    acc = 0
    for n in range(lim+1):
        r=0
        nchooser = 1
        while r <= n/2:
            if nchooser > target:
                acc += n+1-2*r
                break
            nchooser *= n-r
            nchooser /= (r+1)
            r += 1
    return acc
