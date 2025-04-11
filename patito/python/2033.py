# Problem ID: 2033
# Title: Bandera Boliviana

def menor(a, b):
    return a if a < b else b

n = int(input())
for i in range(n):
    colores = input()
    rojo = 0
    amarillo = 0
    verde = 0
    for j in colores:
        if j == 'r':
            rojo += 1
        elif j == 'a':
            amarillo += 1
        elif j == 'v':
            verde += 1
    print(menor(menor(rojo,amarillo), verde))