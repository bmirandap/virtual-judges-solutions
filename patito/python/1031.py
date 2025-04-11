# Problem ID: 1031
# Title: Mediana

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    n = int(linea)
    num = list(map(int, input().split()))
    num = num[0:n]
    num.sort()
    if n % 2 == 0:
        print(-1)
    else:
        pos = n//2
        if (num[pos] != num[pos-1] and num[pos] != num[pos+1]) or pos == 0:
            print(num[pos])
        else:
            print(-1)