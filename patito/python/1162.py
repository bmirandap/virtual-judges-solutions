# Problem ID: 1162
# Title: Imprentas

n = int(input())
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0, n):
    cadena = input()
    imprenta = []
    for letra in cadena:
        if (letra in abecedario) and (not (letra in imprenta)):
                imprenta.append(letra)
    print(len(imprenta))