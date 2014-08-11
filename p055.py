## Count lychrel numbers below 10**4

def lychrel(n, lim=50):
    n += int(str(n)[::-1])
    for round in range(lim):
        if str(n) == str(n)[::-1]:
            return False
        n += int(str(n)[::-1])
    return True

def p055(N=10**4):
    return sum(1 for n in range(N) if lychrel(n))
