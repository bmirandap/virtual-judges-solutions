# Problem ID: 1050
# Title: Binario Inverso

import sys
for lista in sys.stdin:
    if lista == "\n":
        break
    numero = lista
    b = bin(int(numero))[2:]
    b_inv = b[::-1]
    print(int(b_inv, 2))