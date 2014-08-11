## What number below 10**6 has the longest Collatz chain?
#

import memoized

def p014(N=10**6):
    cache = {1:1}
    def collatz(k):
        n=k
        count = 0
        while n not in cache:
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n+1
            count += 1
        cache[k] = cache[n]+count
        return cache[k]
    return max((collatz(n),n) for n in range(1,N+1))[1]

@memoized.memoized
def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n/2)+1
    else:
        return collatz(3*n+1)+1

def withmem(N=10**6):
    return max((collatz(n),n) for n in range(1,N+1))[1]
