## Find the sum of all multiples of 3 or 5 below 1000
#
# standard formula, inclusion-exclusion
#
# compare
# python -m timeit -s 'import p001' 'p001.p001()'
# 1000000 loops, best of 3: 1.43 usec per loop
# python -m timeit -s 'import p001' 'p001.brute()'
# 10000 loops, best of 3: 188 usec per loop


def sum_n(N):
    return N*(N+1)/2

def p001(N=1000):
    N -= 1
    return 3*sum_n(N/3) + 5*sum_n(N/5) - 15*sum_n(N/15)

def brute(N=1000):
    ret_val = 0
    for n in xrange(N):
        if n % 3 == 0 or n % 5 == 0:
            ret_val += n
    return ret_val       
