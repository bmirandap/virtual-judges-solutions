# Problem ID: 1383
# Title: Cola de Impresión

t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    lista = list(map(int, input().split()))
    lista = lista[0:n]    
    c = 0
    pos = m
    while True:
        x = lista.pop(0)
        if len(lista) != 0:
            if pos >= 0 and x < max(lista):
                lista.append(x)
            else:
                c += 1
                if pos == 0:
                    break
            pos -= 1    
            if pos == -1:
                pos = len(lista) - 1
        else:
            c += 1
            break
    print(c)     