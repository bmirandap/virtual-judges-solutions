# Problem ID: 1327
# Title: Desproporción Diagonal

t = int(input())
for i in range(0,t):
    n = int(input())
    dp = 0
    ds = 0
    filas = []
    for j in range(0,n):
        filas.append(list(input()))
    for u in range(0, n):
        for v in range(0,n):
            if u == v:
                dp += int(filas[u][v])
            if u + v == n - 1:
                ds += int(filas[u][v])
    print(dp-ds)