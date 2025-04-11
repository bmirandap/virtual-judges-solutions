# Problem ID: 1904
# Tile: Primero y Ultimo

n = int(input())
for i in range(0, n):
    cadena = input()
    print(cadena[0:3] + " " + cadena[(len(cadena)-3):])