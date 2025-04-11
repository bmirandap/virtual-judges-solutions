# Problem ID: 1584
# Title: Botas y los museos

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    lista = list(map(int, input().split()))
    lista = lista[0:n]
    lista.sort()
    print(lista[len(lista)-1] - lista[0])