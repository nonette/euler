## Find the sum of the only 6-cycle of 4-digit numbers, one triangular, one
# square, etc.
#
# only about a hundred of these numbers per m

from collections import defaultdict
import logging
import math

def figurate(n, m):
    if m == 3:
        return n*(n+1)/2
    elif m == 4:
        return n**2
    elif m == 5:
        return n*(3*n-1)/2
    elif m == 6:
        return n*(2*n-1)
    elif m == 7:
        return n*(5*n-3)/2
    elif m == 8:
        return n*(3*n-2)
    else:
        raise ValueError

def unfigurate(k, m):
    if m == 3:
        return int(math.sqrt(1+8*k)-1)/2
    elif m == 4:
        return int(math.sqrt(k))
    elif m == 5:
        return int(1 + math.sqrt(1+24*k))/6
    elif m == 6:
        return int(unfigurate(k, 3)+1)/2
    elif m == 7:
        return int(3+math.sqrt(9+40*k))/10
    elif m == 8:
        return int(1+math.sqrt(1+3*k))/3

def findcycle(tail, targets, current, byprefix):
    logging.debug(' '.join(('in findcycle', str(tail), str(targets),
        str(current))))
    if len(targets) == 0:
        if current[-1][2:] == tail:
            return current
        else:
            return None
    for num,m in byprefix[current[-1][2:]]:
        if m in targets:
            newtargets = [target for target in targets if target != m]
            cand = findcycle(tail, newtargets, current+[num], byprefix)
            if cand:
                return cand
    return None

def p061(N=8):
    N=8
    nums = [[] for n in range(N+1)]
    n = 1
    while True:
        for m in range(3,N+1):
            cand = str(figurate(n,m))
            if len(cand) == 4:
                nums[m].append(cand)
        if len(str(figurate(n,3))) == 5:
            break
        n += 1
    byprefix = defaultdict(list)
    for m in range(3,N+1):
        for num in nums[m]:
            byprefix[num[:2]].append((num, m))

    for num in nums[N]:
        cand = findcycle(num[:2], range(3,N), [num], byprefix)
        if cand:
            logging.debug(cand)
            return sum(int(x) for x in cand)

