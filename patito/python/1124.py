# Problem ID: 1124
# Title: Copos de Nieve

t = int(input())
for i in range(0, t):
    n = int(input())
    maximo = - 1
    for j in range(0, n):
        x = int(input())
        if x > maximo:
            maximo = x
    print(maximo)