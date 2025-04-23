# Problem ID: 264
# Title: Count on Cantor

import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    if int(linea) == 1:
        print("TERM 1 IS 1/1")
        continue
    diagonal = 2
    elementos = (1 + diagonal) * diagonal // 2
    while elementos < int(linea):
        diagonal += 1
        elementos = (1 + diagonal) * diagonal // 2
    pos = int(linea) - (1 + (diagonal - 1)) * (diagonal - 1) // 2
    if diagonal % 2 != 0:
        print("TERM {} IS {}/{}".format(int(linea), diagonal-(pos-1), pos))
    else:
        print("TERM {} IS {}/{}".format(int(linea), pos, diagonal-(pos-1)))