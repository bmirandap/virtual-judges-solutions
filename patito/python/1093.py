# Problem ID: 1093
# Title: Intercambio de Trenes

n = int(input())
for i in range(0, n):
    l = int(input())
    lista = list(map(int, input().split()))
    lista = lista[0: l]
    t = len(lista)
    c = 0
    for i in range(2, t + 1):
        for j in range(0, t - i + 1):
                if lista[j] > lista[j + 1]:
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp
                    c += 1
    print(c)