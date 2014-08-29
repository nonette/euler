## Find the maximum path sum in the specified triangle

import p018

def p067():
    filename = 'resources/p067triangle.txt'

    with open(filename) as f:
        p066triangle = f.read()

    p066triangle = [[int(n) for n in line.split()] for line in p066triangle.splitlines()]

    return p018.p018(p066triangle)
