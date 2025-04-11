# Problem ID: 1283
# Title: Maximo en cada secuencia

import sys
for lista in sys.stdin:
    if lista == "\n":
        break
    entrada = list(map(int, lista.split()))
    secuencia = entrada[1:entrada[0]+1]
    print(max(secuencia))