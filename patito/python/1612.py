# Problem ID: 1612
# Title: Contando Caracteres

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    s = list(linea.strip())
    s.sort()
    s.append("")
    cont = 0
    car = s[0]
    n = len(s)
    for i in range(0, n):
        if car == s[i]:
            cont += 1
        else:
            print("{}={}".format(car,cont))
            car = s[i]
            cont = 1
    print("")