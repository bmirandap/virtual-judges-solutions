# Problem ID: 1294
# Title: Suma en rango

n = int(input())
for i in range(n):
    m = list(map(int, input().split()))
    numeros = list(map(int, input().split()))
    print(sum(numeros[m[1]:m[2]+1]))