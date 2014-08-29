## Max digital sum of a**b, a,b < 100

def p056():
    return max(sum(int(d) for d in str(a**b)) for a in range(100) for b in range(100))
