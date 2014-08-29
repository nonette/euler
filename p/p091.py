# How many right triangles fit in the box [0..50,0..50]?
# There are 3*50*50 right triangles with the right angle on the x or y axis
# If there is a right angle at (a,b), a,b not 0, the third point must be on
# b -a/b * (x-a) = y

import itertools

def p091(N=50):
    degens = 3*N*N
    gens = 0
    for a,b in itertools.product(range(1,N+1),repeat=2):
        for x in range(N+1):
            if x == a:
                continue
            num = a*x-a**2
            if num % b != 0:
                continue
            y = b - num/b
            if 0 <= y <= N:
                gens += 1
    return degens+gens
