# Find the set of digits a<b<c<d which can produce the longest set of positive
# integers 1..n
#
# For 4 numbers, either we have (x op y) op (z op w) or x op (y op (z op w))

import itertools
import operator

ops = operator.add, operator.mul, operator.div, operator.sub

def gen24(cards):
    poss = set([])
    cards = [float(n) for n in cards]
    for numbers in itertools.permutations(cards):
        for opers in itertools.product(ops,repeat=3):
            output1 = opers[0](opers[1](numbers[0],numbers[1]),opers[2](numbers[2],numbers[3]))
            output2 = opers[0](opers[1](opers[2](numbers[0],numbers[1]),numbers[2]),numbers[3])
            poss.add(output1)
            poss.add(output2)
    return sorted(set([int(x) for x in poss if abs(x-int(x))<0.1 and int(x) >
        0]))

def count24(cards):
    outputs = gen24(cards)
    for i,n in enumerate(outputs):
        if i+1 != n:
            return i
    return i

def p093():
    best,bestval = (),-1
    for cards in itertools.combinations(range(1,10),4):
        val = count24(cards)
        if val > bestval:
            bestval = val
            best = cards
    return ''.join(str(n) for n in best)

