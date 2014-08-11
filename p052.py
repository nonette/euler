## The smallest x s.t. [str(n*x) for n in range(1,7)] are permutations
#
#
# Turns out to be good old 1/7. Of course?

import logging

logger = logging.getLogger(__name__)

def p052(N=6):
    x = 1
    counter = 1
    while True:
        if len(set([''.join(sorted(str(n*x))) for n in range(1,counter+1)])) == 1:
            if counter == N:
                return x
            else:
                logger.debug(x)
                counter += 1
        else:
            x += 1
