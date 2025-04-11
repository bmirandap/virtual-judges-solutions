# Problem ID: 2169
# Title: La serie de Deyvid

def criba(n):
    primos = []
    esPrimo = [1 for i in range(n)]
    esPrimo[0] = esPrimo[1] = 0
    for i in range(n):
        if esPrimo[i]:
            primos.append(i)
            h = 2
            while i*h < n:
                esPrimo[i*h] = 0
                h += 1
    return primos
    
primos = criba(2000000)
t = int(input())
for i in range(0,t):
    serie = ["1"]
    n = int(input())
    for j in range(0, n-1):
        if primos[j]>10:
            serie.append(str(int(serie[j])+(primos[j]%10)))
        else:
            serie.append(str(int(serie[j])+primos[j]))
    print(" ".join(serie))