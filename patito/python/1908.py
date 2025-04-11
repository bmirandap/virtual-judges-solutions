# Problem ID: 1908
# Title: Siglas Empresariales

n = int(input())
for i in range(0, n):
    lista = list(input().split())
    sigla = ""
    for palabra in lista:
        sigla += palabra[0].upper()
    print(sigla)