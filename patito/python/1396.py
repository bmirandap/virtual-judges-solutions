# Problem ID: 1396
# Title: Dos cadenas

import sys
def verifica(c):
    resp = True
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(0,26):
        if not (abecedario[i] in c):
            resp = False
            break
    return resp

for linea in sys.stdin:
    if linea == "\n":
        break
    linea = linea[0:len(linea)-1]
    linea2 = input()
    c1 = set(linea)
    c2 = set(linea2)
    c = c1.union(c2)
    if verifica(c):
        print("Correcto")
    else:
        print("Incorrecto")
   