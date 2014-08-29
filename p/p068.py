## Find the maximum 16-digit string corresponding to a magic 5-gon

import itertools
import logging

def ngons(N):
    sols = set([])
    M = 2*N
    for p in itertools.permutations(range(1,M+1),N):
        qpool = set(range(1,M+1))-set(p)
        sums = [p[i]+p[(i+1)%N] for i in range(N)]
        ind = sums.index(max(sums))
        p = p[ind:]+p[:ind]
        sums = sums[ind:]+sums[:ind]
        magic = sums[0]+min(qpool)
        q = []
        for s in sums:
            target = magic-s
            if target not in qpool:
                break
            qpool.remove(target)
            q.append(target)
        else:
            sol = tuple((q[i],p[i],p[(i+1)%N]) for i in range(len(q)))
            sols.add(sol)
    for sol in sols:
        logging.debug(sol)
    return sols
    
def p068():
    sols = ngons(5)
    filtered = [sol for sol in sols if sorted(sum(sol,()))[-2] < 10]
    best = max(filtered)
    return ''.join(''.join(str(d) for d in s) for s in best)


