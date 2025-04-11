# Problem ID: 1221
# Title: Tres Números

numeros = list(map(int, input().split()))
numeros.sort()
print("{} {} {}".format(numeros[0], numeros[1], numeros[2]))