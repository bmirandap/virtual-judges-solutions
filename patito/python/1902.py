# Problem ID: 1902
# Title: Contar subcadenas

n = int(input())
for i in range(0, n):
    cadena = input()
    subcadena = input()
    print(cadena.count(subcadena))