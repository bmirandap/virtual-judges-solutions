# Problem ID: 1316
# Title: Ordenando Vectores

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    a = list(map(int, input().split()))
    a = a[0:n]
    b = list(map(int, input().split()))
    b = b[0:n]
    a.sort()
    b.sort(reverse=True)
    s = []
    for i in range(0,n):
        s.append(a[i]*b[i])
    print(sum(s))