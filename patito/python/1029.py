# Problem ID: 1029
# Title: Escoger Equipos

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    arr = list(map(int, linea.split()))
    arr.sort(reverse = True)
    n = len(arr)
    cap1, cap2 = 0, 0
    for i in range(0, n):
        if i % 2 == 0:
            cap1 += arr[i]
        else:
            cap2 += arr[i]
    print(cap1 - cap2)