## Find prod(d_{10**k} for k in range(0,7)) where
# d is formed by concatenating integers
#
# 9*10**k k-digit numbers
#
# Solution: 210

import utils

def d(n):
    n -= 1 # since we're 1-indexing
    k=1
    while n - k*9*10**(k-1) >= 0:
        n -= k*9*10**(k-1)
        k += 1
    # now look for the nth index of concatenated k-digit numbers
    numberstring = str(n/(k*10**(k-1))+1)
    n = n % (k*10**(k-1))
    for j in range(1,k):
        numberstring += str(n/(k*10**(k-j-1)))
        n = n % (k*10**(k-j-1))
    return int(numberstring[n])

def p040():
    return utils.prod(d(10**k) for k in range(0,7))
