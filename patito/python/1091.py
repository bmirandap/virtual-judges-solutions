# Problem ID: 1091
# Title: Divisibilidad

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    a, b = map(int, linea.split())
    if a % b == 0:
        print("{} es divisible por {}".format(a, b))
    elif b % a == 0:
        print("{} es divisible por {}".format(b, a))
    else:
        print("-1")