# Find the largest square number formed by an anagram pair in the given file

import collections
import itertools
import logging
import math

filename = 'resources/p098words.txt'

def canonicalize(word):
    return ''.join(sorted(word))

def gen_squaremap(word, square):
    squaremap = {}
    for char,digit in zip(word, str(square)):
        if char in squaremap:
            if digit != squaremap[char]:
                return None
        squaremap[char] = digit
    if len(set(squaremap.values())) != len(set(squaremap.keys())):
        return None
    return squaremap

def anagram_square(a,b):
    n = len(a)
    bestval = -1
    for s in range(int(math.ceil(10**((n-1)/2.0))),int((10**n-1)**0.5)+1):
        square = s**2
        squaremap = gen_squaremap(a,square)
        if squaremap:
            bval = int(''.join(squaremap[char] for char in b))
            if int(bval**0.5)**2 == bval and len(str(bval)) == len(b):
                logging.debug('%s %d %s %d' % (a, square, b, bval))
                bestval = max(bestval, max(square, bval))
    return bestval

def p098(words=None):
    if not words:
        with open(filename) as f:
            words = [word.strip('"') for word in f.read().split(',')]
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[canonicalize(word)].append(word)

    bestval = -1
    for key in anagrams:
        for a,b in itertools.combinations(anagrams[key],2):
            bestval = max(bestval, anagram_square(a,b))
    return bestval

