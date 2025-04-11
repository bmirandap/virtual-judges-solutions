# Problem ID: 1121
# Title: Avengers

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    superheroes = set()
    for i in range(0, n):
        fila = list(map(str, input().split()))
        m = len(fila)
        for j in range(1, m):
            superheroes.add(fila[j])
    x = input()
    array_heroes = list(superheroes)
    array_heroes.sort()
    pos = array_heroes.index(x)
    print(len(array_heroes[0:pos]))