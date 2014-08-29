# Find the smallest member of the longest amicable chain with no element
# exceeding 10**6

import utils

def p095(N=10**6):
    table = [utils.sigma(f)-n for n,f in enumerate(utils.factortable(N))]
    lengths = [-1 for n in table]
    for i in range(len(table)):
        chain = [i]
        j=table[i]
        while j < len(table) and j not in chain:
            chain.append(j)
            j = table[j]
        if j == i:
            lengths[i] = len(chain)
    return lengths.index(max(lengths))
