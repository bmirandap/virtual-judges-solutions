# Problem ID: 1291
# Title: Lectura3

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    array = list(map(int, linea.split()))
    print(sum(array))