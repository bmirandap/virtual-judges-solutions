# Problem ID: 1147
# Title: Centro Medio

import sys
def sumatoria(n):
    return (n*(n+1))//2

for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    a = 0
    b = n
    while (b-a)>1:
        medio = (a+b)//2
        sumizq = sumatoria(medio-1)
        sumder = sumatoria(n) - sumatoria(medio)
        if sumizq >= sumder:
            b = medio
        else:
            a = medio
    totalizq = sumatoria(b-1)
    totalder = sumatoria(n) - sumatoria(b)
    
    if totalizq != totalder:
        print("NO")
    else:
        print(b)
    