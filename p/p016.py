## Sum of the digits in 2**1000

def p016(N=1000):
    return sum(int(d) for d in str(2**N))
