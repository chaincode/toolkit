from sympy import *

x = Symbol('x')
y = Symbol('y')
S = Symbol('S')
K = Symbol('K')
e = Symbol('e')
r = Symbol('r')
h = Symbol('h')
o = Symbol('o')
T = Symbol('T')

d1 = (ln(S/K) + (r + 0.5 * o * o) * T) / (sqrt(T) * o)
d2 = d1 - (sqrt(T) * o)

def getN(d):
	return (2/pi) * integrate(exp(-x**2/2),(x,-oo,d))

def getC(d1,d2):
	C = S*e**(-h*T)*getN(d1) - K*e**(-r*T)*getN(d2)
	return C

def getP(d1,d2):
	P = -S*e**(-h*T)*getN(-d1) - K*e**(-r*T)*getN(-d2)
	return P

print d1
print d2

print "N(d1)=", getN(d1)
print "N(d2)=", getN(d2)

print "C=", getC(d1,d2)
print "P=", getP(d1,d2)


