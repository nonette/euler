## Find the shortest distance between two pentagonal numbers s.t. 
# their sum and difference are also pentagonal
#
# P_n = n(3n-1)/2
#
# consecutive differences are 3n+1
#
# We are looking for the smallest i s.t.
# P_i+P_j = P_k
# P_k+P_j = P_l
#
# I can very quickly find the smallest *k*
# How to show that it corresponds to the smallest i?
# Are these actually the only three pentagonal numbers in arithmetic progression
# where the common difference is pentagonal?
#
# k < i+j, l < i+2*j
# k-i > l-k >= 1
#
# P[1912] = 5482660
# P[1020] = 1560090
# P[2167] = 7042750
# P[2395] = 8602840


from collections import deque
import math

def pent(n):
    return n*(3*n-1)/2

def unpent(k):
    return int((1 + math.sqrt(1+24*k))/6)

def ispent(k):
    return pent(unpent(k)) == k
       
def correctbutslowasballs():
    lim = 2*10**6
    cache = set([n*(3*n-1)/2 for n in range(lim)])
    i = 1
    while True:
        p_i = pent(i)
        j = 1
        while j <= (p_i-1)/3:
            p_j = pent(j)
            if i+j > lim:
                print i, j
                return
            if p_i+p_j in cache:
                print i, j
                if i+2*j > lim:
                    print i, j, j
                    return
                if p_i+2*p_j in cache:
                    return p_i
            j += 1
        i += 1

def p044():
    seenset = set()
    seenlist = deque()
    n = 1
    while True:
        a = pent(n)
        for b in seenlist:
            if a-b in seenset:
                 if ispent(a+b):
                     return a-b
        n += 1
        seenlist.appendleft(a)
        seenset.add(a)
