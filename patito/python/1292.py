# Problem ID: 1292
# Title: Lectura4

import sys
for linea in sys.stdin:
    n = int(linea)
    if n == 0:
        break
    array = list(map(int, input().split()))
    array = array[0:n]
    print(sum(array))