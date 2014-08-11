## Find the largest 1..9 pandigital
#
#

import itertools
import logging

logger = logging.getLogger(__name__)

def p038():
    for p in itertools.permutations(range(9,0,-1)):
        cand = ''.join(str(d) for d in p)
        for l in range(1,len(p)/2 + 1):
            x = cand[:l]
            leftovers = cand[l:]
            n = 2
            while leftovers:
                target = str(n*int(x))
                if target == leftovers[:len(target)]:
                    leftovers = leftovers[len(target):]
                    n += 1
                else:
                    break
            else:
                logger.debug('%s %s' % (x, cand))
                return cand
