# Problem ID: 1107
# Title: Monton

import sys
for lista in sys.stdin:
    if lista == "\n":
        break
    entrada = lista[0:len(lista)]
    pila = []
    for c in entrada:
        if c.isdigit():
            pila.append(int(c))
        if c == '+':
            b = pila.pop()
            a = pila.pop()
            pila.append(a+b)
        if c == '*':
            b = pila.pop()
            a = pila.pop()
            pila.append(a*b)
    print(pila.pop())