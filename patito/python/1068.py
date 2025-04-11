# Problem ID: 1068
# Title: Homero

t = int(input())
for i in range(0, t):
    n = int(input())
    c = 0
    contar = True
    for j in range(0, n):
        instruccion = input()
        if instruccion == "porque":
            contar = False
        else:
            if contar:
                c += 1
    print(c)