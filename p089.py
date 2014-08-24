# Find the total number of characters saved by writing the numbers in the
# standard Roman form.
#
# 

import itertools

filename = 'p089roman.txt'

rtoi = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
itor = dict((v,k) for k,v in rtoi.items())
vals = sorted(itor.keys())[::-1]
subtract = {1000:100, 500:100, 100:10, 50:10, 10:1, 5:1, 1:0}

def romtoint(s):
    last_val = 5000
    last_mult = 0 
    acc = 0
    for k,g in itertools.groupby(s):
        if last_val < rtoi[k]:
            acc -= 2*(last_val*last_mult)
        last_val = rtoi[k]
        last_mult = len(list(g))
        acc += last_val*last_mult
    return acc        

def inttorom(n):
    acc = ''
    for val in vals:
        while n >= val:
            n -= val
            acc += itor[val]
        if n >= val - subtract[val]:
            acc += itor[subtract[val]]+itor[val]
            n -= val - subtract[val]
    return acc


def p089():
    with open(filename) as f:
        nums = f.read().splitlines()
    savings = 0
    for num in nums:
        i = romtoint(num)
        savings += len(num)-len(inttorom(i))
    return savings
