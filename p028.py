## Find the sum of the diagonal numbers in a 1001x1001 clockwise spiral
#

def spiral(N):
    table = [[0]*N for n in range(N)]
    i = N/2
    j = N/2
    n = 1
    table[i][j] = n
    n += 1
    
    for k in range(1, (N+1)/2):
        #go right one
        j += 1
        table[i][j] = n
        n += 1
        # go down
        for inc in range(2*k-1):
            i += 1
            table[i][j] = n
            n += 1
        # go left
        for inc in range(2*k):
            j -=1
            table[i][j] = n
            n += 1
        #go up
        for inc in range(2*k):
            i -=1
            table[i][j] = n
            n += 1
        #go right
        for inc in range(2*k):
            j += 1
            table[i][j] = n
            n += 1
    return table

def p028(N=1001):
    return sum(4*(2*k-1)**2 + 20*k for k in range(1, (N+1)/2)) + 1

def justadd(N = 1001):
    acc = 1
    cur = 1
    for k in range(1, (N+1)/2):
        #go right one then down
        cur += 2*k
        acc += cur
        #go left
        cur += 2*k
        acc += cur
        #go up
        cur += 2*k
        acc += cur
        #go right
        cur += 2*k
        acc += cur
    return acc        

def drawitout(N = 1001):
    table = spiral(N)
    return (sum(table[i][i]+table[i][-1-i] for i in range(N)) -
            table[N/2][N/2])
