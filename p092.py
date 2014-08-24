# How many digitssquaresum chains starting below 10**7 end at 89?
#
# f(n) maps into 1..657. That is small.
#
# 7 digits, 10 possibilities, about 2*10**4 possibilities for digit
# distribution. Also small.

import itertools

import utils

def f(n):
    return sum(int(d)**2 for d in str(n))

def chain89(n, table=[-2,-1]+[0]*87+[1]+[0]*600):
    if n >= len(table):
        n = f(n)
    acc = []
    while table[n]==0:
        acc.append(n)
        n = f(n)
    outcome = table[n]
    for n in acc:
        table[n] = outcome
    return outcome == 1   

def chain(n):
    acc = [n]
    while n != 1 and n != 89:
        n = f(n)
        acc.append(n)
    return acc

def multiplicity(digits):
    mults = (len(list(g)) for k,g in itertools.groupby(digits))
    ret_val = utils.fact(len(digits))
    for m in mults:
        ret_val /= utils.fact(m)
    return ret_val


def p092(N=7):
    acc = 0
    for digits in itertools.combinations_with_replacement(range(10),N):
        outcome = chain89(sum(d**2 for d in digits))
        if outcome:
            acc += multiplicity(digits)
    return acc
