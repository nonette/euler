## Find the least value of n s.t. partitions(n) is divisible by 10**6

import p076

def penthelper(k):
    return k*(3*k-1)/2

def pent():
    n = 1
    while True:
        yield penthelper(n)
        yield penthelper(-n)
        n += 1

cache = {}
def partitions(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n not in cache:
        p_gen = pent()
        p = p_gen.next()
        acc = 0
        counter = 0
        while p <= n:
            acc += (1 if counter % 4 < 2 else -1)*partitions(n-p)
            counter += 1
            p = p_gen.next()
        cache[n] = acc
    return cache[n]


def p078(N=10**6):
    n = 1
    parts = partitions(n)
    while parts % N != 0:
        n += 1
        parts = partitions(n)
    return n
