# Problem ID: 1056
# Title: al revés

n = int(input())
for i in range(0, n):
    a = int(input())
    numeros = list(map(int, input().split()))
    numeros = numeros[0:a]
    numeros_inv = numeros[::-1]
    num = ""
    for elem in numeros_inv:
        num += str(elem) + " "
    print(num)