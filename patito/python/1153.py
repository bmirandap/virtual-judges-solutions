# Problem ID: 1153
# Title: Esparta

import sys
for lista in sys.stdin:
    if lista == "\n":
        break
    lista = lista[0:len(lista)-1]
    habilidades = []
    s = ""
    for e in lista:
        if e.isdigit():
            habilidades.append(int(e))
        elif e == '*':
            habilidades.append(habilidades.pop() * habilidades.pop())
        elif e == '+':
            habilidades.append(habilidades.pop() + habilidades.pop())
        else:
            s += e
    s = s[len(s)::-1]
    s += ": habilidad " + str(habilidades.pop())
    print(s)