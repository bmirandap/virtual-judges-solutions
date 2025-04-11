# Problem ID: 1286
# Title: Pares incremento

n = int(input())
for i in range(n):
    entrada = list(map(int, input().split()))
    secuencia = entrada[1:entrada.index(0)]
    ant = entrada[0]
    c = 0
    for num in secuencia:
        if num > ant:
            c += 1
        ant = num
    print(c)