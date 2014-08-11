## Find abc where a + b + c = 1000 and (a,b,c) is a Pythagorean triple.
#
# Every Pythagorean triple is of the form k(2mn, m**2-n**2, m**2+n**2)
# The triple is primitive if (m,n)=1 and m-n % 2 == 1

def p009():
    for a in range(1000):
        for b in range(a,1000):
            c = 1000-a-b
            if c <= b:
                break
            if a**2+b**2 == c**2:
                return a*b*c
