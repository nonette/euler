## Find the total of the name scores in the given file

import utils

def readnames(filename):
    names = ''
    with open(filename) as f:
        names = f.read()
    names = [name.strip('"') for name in names.split(',')]
    names.sort()
    return names

def namescore(name):
    return sum(ord(c)-64 for c in name)

def p022(filename="p022names.txt"):
    names = readnames(filename)
    return sum((i+1)*namescore(n) for (i,n) in enumerate(names))
        
