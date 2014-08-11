## First term in the Fibonacci with 1000 digits
#

def p025(N=1000):
    count = 1
    a,b=1,1
    while len(str(a)) < N:
        a,b = b,a+b
        count += 1
    return count
