# Problem ID: 1504
# Title: Ordenando el Laboratorio

def sumaFilaColumna(fila, columna, elemento):
    resp = False
    for f in fila:
        for c in columna:
            if f + c  == elemento:
                resp = True
                break
        if resp:
            break
    return resp

t = int(input())
for i in range(0, t):
    n = int(input())
    matriz = []
    for j in range(0, n):
        matriz.append(list(map(int, input().split())))
    
    sw = True
    for x in range(0, n):
        for y in range(0, n):
            if matriz[x][y] != 1:
                fila = []
                columna = []
                for k in range(0, n):
                    if matriz[x][k] != matriz[x][y]:
                        fila.append(matriz[x][k])
                    if matriz[k][y] != matriz[x][y]:
                        columna.append(matriz[k][y])
                
                if not sumaFilaColumna(fila, columna, matriz[x][y]):
                    sw = False
                    break
        if not sw:
            break
    if sw:
        print("Si")
    else:
        print("No")