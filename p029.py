## Find the number of distinct a**b, 2 le a le 100, 2 le b le 100

def p029(N=100):
    return len(set([a**b for a in range(2,N+1) for b in range(2,N+1)]))
