## Find the largest palindrome which is the product of 2 3-digit numbers
#

def p004(N=3):
    for a in range(10**N-1,0,-1):
        n = a*10**N + int(str(a)[::-1])
        for f in range(10**(N-1)+1,int(n**0.5)+1):
            if n % f == 0:
                if len(str(n/f)) == N:
                    return n


