# Find M s.t. the number of cuboids of dimension less than MxMxM with integral
# shortest corner-to-corner distance first exceeds 10**6
#
# If a cuboid has dimension axbxc, a<=b<=c, then its shortest corner-to-corner
# distance is sqrt((a+b)**2+c**2)
#
# And apparently we're only counting ordered dimensions
# (no multiplicity 3x2x2, 2x3x2, 2x2x3) 

import logging
import math

def countM(M):
    count = 0
    for N in range(2,2*M):
        lsquared = M**2+N**2
        if int(math.sqrt(lsquared))**2 == lsquared:
            if N <= M:
                # a ranges from 1 to N/2
                count += N/2
            else:
                # a ranges from N-M to N/2
                count += N/2-(N-M)+1
    return count

def p086(target=10**6):
    M=1
    count = 0
    while True:
        count += countM(M)
        logging.debug('%d %d' % (M, count))
        if count > target:
            break
        M += 1
    return M
