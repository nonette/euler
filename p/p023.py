## Find the sum of all positive integers which cannot be written as the sum of
# two abundant numbers
#
# A number is abundant if sigma(n) > 2*n
#
# Solution: 4179871

import lib.numty as numty

LIMIT = 21823

def p023():
    abundant = [n for (n,f) in enumerate(numty.factortable(LIMIT))
            if numty.sigma(f) > 2*n > 0]
    abundantset = set(abundant)

    def check_n(n):
        for a in abundant:
            if n-a in abundantset:
                return False
            if n-a < a:
                return True
    
    return sum(n for n in range(LIMIT+1) if check_n(n))

