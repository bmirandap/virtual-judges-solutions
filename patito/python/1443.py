# Problem ID: 1443
# Title: DPA

import sys

def sumaDivisores(n):
    s = 0
    for divisor in range(1, (n // 2) + 1):
        if n % divisor == 0:
            s += divisor
    return s

for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    s = sumaDivisores(n)
    if s == n:
        print("Perfecto")
    elif s < n:
        print("Deficiente")
    else:
        print("Abundante")
