# Problem ID: 1253
# Title: tablero

n = int(input())
for i in range(0,n):
    r, c = map(int, input().split())
    fila = []
    s = 0
    for j in range(0, r):
        fila.append(input())
        fila[j] = fila[j][0: c]
        t = len(fila[j])
        for k in range(0, t):
            if (j % 2 == 0 and k % 2 == 0) or (j % 2 != 0 and  k % 2 != 0):
                s += int(fila[j][k])
    print(s)