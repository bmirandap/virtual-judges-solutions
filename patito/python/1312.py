# Problem ID: 1312
# Title: Comprando

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    precios = list(map(int, input().split()))
    precios.sort()
    c = 1
    for i in range(0, n-1):
        if precios[i] != precios[i+1]:
            c += 1
        if c == 3:
            precio = precios[i+1]
            break
    print(precio if c == 3 else -1)