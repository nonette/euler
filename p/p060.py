## Find the set of five primes s.t. any concatenation of two of them produces a
# prime with the smallest set sum.
#
# Solution: 26033
# really not that big...

from collections import defaultdict

import lib.numty as numty

## this is uselessly slow
def splitsum(n, target, searchspace, acc=[]):
    if n == 1:
        if target in searchspace:
            yield acc + [target]
    for i,p in enumerate(searchspace):
        if p > target:
            break
        for v in splitsum(n-1, target-p, searchspace[i+1:], acc+[p]):
            yield v

def p060():
    G = gengraph(10**4)
    c = clique(5, sorted(G.keys()), G)
    return sum(c)

def gengraph(N):
    primes = numty.sieve(N)
    graph = defaultdict(list)
    for i in xrange(len(primes)):
        p = primes[i]
        for j in xrange(i):
            q = primes[j]
            if (p+q)%3 == 0:
                continue
            pq = int(str(p)+str(q))
            qp = int(str(q)+str(p))
            if numty.isprime(pq) and utils.isprime(qp):
                    graph[p].append(q)
                    graph[q].append(p)
    return graph

def clique(n, searchspace, graph, acc=[]):
    if n == 0:
        return acc
    if n > len(searchspace):
        return None
    for p in searchspace:
        cand = clique(n-1,
                sorted(set(graph[p]).intersection(set(searchspace))),
                graph,
                acc+[p])
        if cand:
            return cand
    return None


