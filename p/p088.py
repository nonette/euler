# Find the sum of all minimum product-sum numbers in range(2,12001)
#
# Every nontrivial decomposition of a composite number leads to a product-sum
# representation.

import lib.numty as numty


def decomps(N):
    decomps = [[] for n in range(N)]
    primes = set(numty.sieve(N))
    for n in range(2,N):
        decomps[n].append([n])
        if n in primes:
            continue
        for k in range(2,n):
            if k > n/2:
                break
            if n % k == 0:
                decomps[n] += [[k]+v for v in decomps[n/k] if 
                        all(k<=f for f in v)]
    return decomps

def p088(N=12000, extra=300):
    best_k = [0 for n in range(N+1)]
    ub=N+extra
    d = decomps(ub)
    for n in range(2,ub):
        for decomp in d[n]:
            k = n-sum(decomp)+len(decomp)
            if k > N:
                continue
            if best_k[k] == 0:
                best_k[k] = n
    if 0 in best_k[1:]:
        raise ValueError("Needs more extra")
    return sum(set(best_k[2:]))
