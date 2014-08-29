## Count the nontrivial partitions of 100
#
# Let p(n,k) be the partitions of n into exactly k parts.
# Either there is a partition of size 1 or every partition has size at least 2.
# In the first case, there are p(n-1,k-1) possibilities. In the second case,
# p(n-k,k).

cache = {}
def p(n,k):
    if n == 0 and k == 0:
        return 1
    if n <= 0 or k <= 0:
        return 0
    if (n,k) not in cache:
        cache[(n,k)] = p(n-k, k) + p(n-1, k-1)
    return cache[(n,k)]

def partitions(n):
    return sum(p(n,k) for k in range(1,n+1))

def p076(N=100):
    return partitions(N)-1
