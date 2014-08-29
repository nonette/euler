## Find 4-digit primes in arithmetic sequence that are permutations of each
# other

from collections import defaultdict

import lib.numty as numty

def p049():
    found = 1487

    primes = numty.sieve(10**4)
    table = defaultdict(list)
    for p in primes:
        str_p = str(p)
        if len(str_p) < 4:
            continue
        table[''.join(sorted(str_p))].append(p)
    for key in table:
        if len(table[key]) >= 3:
            cands = sorted(table[key])
            for b in cands:
                for a in cands:
                    if a >= b:
                        break
                    if 2*b-a in cands:
                        if a == found:
                            continue
                        return str(a)+str(b)+str(2*b-a)
