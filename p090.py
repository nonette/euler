# How many arrangments of two cubes allow all square numbers to be displayed
#
# Canonical description: both dice sorted, lexicographically first dice first

import itertools

target = '01 04 09 19 25 39 49 81'.split()

def checkdice(dice):
    redice = (''.join(d if d!='6' else '9' for d in dice[0]),
            ''.join(d if d!='6' else '9' for d in dice[1]))
    combos = set(([''.join(x) for x in itertools.product(redice[0],redice[1])] + 
            [''.join(x) for x in itertools.product(redice[1],redice[0])]))

    for t in target:
        if t not in combos:
            print t, dice

def placesquare(dice, a):
    acc = set([])
    for d1, d2 in dice:
        if a[0] not in d1:
            d1 = ''.join(sorted(d1+a[0]))
        if a[1] not in d2:
            d2 = ''.join(sorted(d2+a[1]))
        if len(d1) <= 6 and len(d2) <= 6:
            acc.add((d1,d2))
    return acc

def placesplits(dice, splits):
    for s1,s2 in splits:
        dice = placesquare(dice,(s1,s2)).union(placesquare(dice,(s2,s1)))
    return dice

def subsixes(dice):
    acc = set([])
    for d1,d2 in dice:
        subd1 = ''.join(s if s !='9' else '6'for s in d1) 
        subd2 = ''.join(s if s !='9' else '6' for s in d2)
        acc.update(((d1,d2),(subd1,d2),(d1,subd2),(subd1,subd2)))
    return acc

def filldie(d):
    space = set('0123456789').difference(d)
    repeat = 6-len(d)
    return [d+''.join(fill) for fill in itertools.combinations(space, repeat)]

def filltemplate(d1, d2):
    return itertools.product(filldie(d1),filldie(d2))

def canonicalize(d1,d2):
    d1 = ''.join(sorted(d1))
    d2 = ''.join(sorted(d2))
    return (min(d1,d2),max(d1,d2))

def p090():
    templates = placesplits(set([('','')]), target)
    templates = subsixes(templates)
    dice = set([])
    for template in templates:
        dice.update(canonicalize(*d) for d in filltemplate(*template))
    return len(dice)
    
