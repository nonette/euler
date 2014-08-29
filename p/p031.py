## How many ways can 2 pounds be made using the given coins?
#

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def p031(N=200):
    cache = [1]*(N+1)
    for maxcoin in coins[1:]:
        newcache = [0]*(N+1)
        for n in range(N+1):
            newcache[n] = sum(cache[n-k*maxcoin] 
                    for k in range(n/maxcoin + 1))
        cache = newcache
    return cache[N]
