# Problem ID: 1467
# Title: Cambio

import sys
for lista in sys.stdin:
    if lista == "\n":
        break
    entrada = list(map(int, lista.split()))
    monedas = entrada[1:len(entrada) - 1]
    monedas.sort(reverse=True)
    total = entrada[len(entrada) - 1]
    c = 0
    for mon in monedas:
        c += total // mon
        total -= mon * (total // mon) 
    print(c if total == 0 else -1)