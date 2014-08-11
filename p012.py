## First triangle number to have over 500 divisors
#
# randomly used 10**5 as an upperbound there
# not sure how to justify this choice


import utils

def numdivs(factorization):
    return utils.prod((e+1) for e in factorization.values())

def p012(N=500):
    table = utils.factortable(10**5)
    n = 1
    while True:
        if numdivs(table[n])*numdivs(table[(n+1)/2]) > N:
            return n*(n+1)/2
        n += 1
        if numdivs(table[n/2])*numdivs(table[n+1]) > N:
            return n*(n+1)/2
        n += 1
    
