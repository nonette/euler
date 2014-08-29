## Find the smallest cube for which exactly five permutations of its digits are
# cubes

from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

def p062():
    d = defaultdict(list)
    for n in range(10**4):
        c = n**3
        d[''.join(sorted(str(c)))].append(c)
    cand = 10**12
    for key in d.keys():
        if len(d[key]) == 5:
            cand = min(cand,min(d[key]))
    logger.debug(d[''.join(sorted(str(cand)))])
    return cand

