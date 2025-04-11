# Problem ID: 1907
# Title: Remplazar todas las ocurrencia

n = int(input())
for i in range(0, n):
    cadena = input()
    buscar, remplazar = input().split()
    print(cadena.replace(buscar, remplazar))