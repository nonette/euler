## Find the millionth lexicographic permutation of range(10)
#

import lib.numty as numty

# where n is in 0..len(l)!
def nthperm(N, l):
    if len(l) == 1:
        return l
    lminus1fact = numty.prod(range(1,len(l)))
    firstelt = N/lminus1fact
    return [l[firstelt]] + nthperm(N % lminus1fact, l[:firstelt]+l[firstelt+1:])

def p024():
    return ''.join(str(d) for d in nthperm(10**6-1, range(10)))
