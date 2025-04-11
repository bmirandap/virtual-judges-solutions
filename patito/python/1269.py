# Problem ID: 1269
# Title: Fracciones

import sys
def mcd(a, b):
	if b == 0: 
	    return a
	return mcd(b, a%b)

for lista in sys.stdin:
    if lista == "0 0 0 0\n":
        break
    n1, d1, n2, d2 = map(int, lista.split())
    term1 = mcd(n1, d1)
    n1 //= term1
    d1 //= term1
    term2 = mcd(n2, d2)
    n2 //= term2
    d2 //= term2
    if n1 == n2 and d1 == d2:
        print("=")
    else:
        print("!=")