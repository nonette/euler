## How many continued fractions of sqrt(N) for N <= 10**4 have an odd period?
#
# 1/(a+b sqrt(n)) = (a-b sqrt(n))/(a**2-n*b**2)
# b sqrt(n) - bflrsqrtn > 0
# b sqrt(n) + a-(bflrsqrtn+a) > 0
# ugggggggh 3x slow with the class how to tweak
# observed but not proven: b is always a unit fraction

import logging
from decimal import Decimal
import numbers
from fractions import Fraction

logger = logging.getLogger(__name__)

def cf(x):
    yield int(x)
    x = x-int(x)
    while x != 0:
        x = 1/x
        yield int(x)
        x = x-int(x)

def flrsqrt(n):
    x=n
    ub = n
    while x**2 > n:
        ub = x
        x /= 2
    lb = x
    while True:
        middle = (ub+lb)/2
        if middle**2 <= n and (middle+1)**2 > n:
            return middle
        if middle**2 < n:
            lb = middle
        else:
            ub = middle

class Quad:
    def __init__(self,a,b,n):
        self.a = Fraction(a)
        self.b = Fraction(b)
        self.n = n

    def __repr__(self):
        return '%s + %s sqrt(%d)' % (str(self.a), str(self.b), self.n)

    def __eq__(self,other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        return (self.a == other.a and
                self.b == other.b and
                self.n == other.n)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        if self.n != other.n:
            raise ValueError
        return Quad(self.a+other.a, self.b+other.b, self.n)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b, self.n)

    def __sub__(self, other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        if self.n != other.n:
            raise ValueError
        return Quad(self.a-other.a, self.b-other.b, self.n)

    def __rsub__(self, other):
        return other + -self

    def __mul__(self, other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        if self.n != other.n:
            raise ValueError
        return Quad(self.a*other.a+self.n*self.b*other.b,
                self.a*other.b+self.b*other.a,
                self.n)

    __rmul__ = __mul__

    def reciprocal(self):
        return Quad(Fraction(self.a,self.a**2-self.n*self.b**2),
                Fraction(-self.b,self.a**2-self.n*self.b**2), self.n)

    def __div__(self, other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        if self.n != other.n:
            raise ValueError
        return self.__mul__(other.reciprocal())

    def __rdiv__(self, other):
        if isinstance(other, numbers.Rational):
            other = Quad(other,0,self.n)
        return other.__div__(self)

def inv(a,b,n):
    denom = a**2-b**2*n
    return (a/denom, -b/denom)

def handcfsqrt(n):
    floor = flrsqrt(n)
    cf = [floor]
    if floor**2 == n:
        return cf
    a,b=Fraction(0),Fraction(1)
    target = (-floor,1)
    a,b = inv(a-floor,b,n)
    coeff = int(b*floor+a)
    a -= coeff
    cf.append(coeff)
    while (a,b) != target:
        a,b = inv(a,b,n)
        coeff = int(b*floor+a)
        a -= coeff
        cf.append(coeff)
    return cf

def cfsqrt(n):
    floor = flrsqrt(n)
    cf = [floor]
    if floor**2 == n:
        return cf
    x = Quad(0,1,n)
    target = x-floor
    x = 1/target
    coeff = int(x.b*floor+x.a)
    x -= coeff
    cf.append(coeff)
    while x != target:
        x = 1/x
        coeff = int(x.b*floor+x.a)
        x -= coeff
        cf.append(coeff)
    return cf
    
def p064(N=10**4):
    count = 0
    for n in range(1,N+1):
        cf = handcfsqrt(n)
        logger.debug('%d %s' % (n, str(cf)))
        if (len(cf)-1)%2 == 1:
            count += 1
    return count

def slowp064(N=10**4):
    count = 0
    for n in range(1,N+1):
        cf = cfsqrt(n)
        logger.debug('%d %s' % (n, str(cf)))
        if (len(cf)-1)%2 == 1:
            count += 1
    return count
