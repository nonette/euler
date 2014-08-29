# Find the largest exponential in the given file
#
# Given b,e let's calculate e log b

import math

filename = 'p099baseexp.txt'

def loadpairs():
    with open(filename) as f:
        def process(l):
            a,b = l.split(',')
            return int(a),int(b)
        return [process(l) for l in f.read().splitlines()]

def p099(pairs=None):
    if not pairs:
        pairs = loadpairs()
    values = [math.log(b)*e for b,e in pairs]
    return values.index(max(values))+1
