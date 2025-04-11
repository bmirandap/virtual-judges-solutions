# Problem ID: 1906
# Title: Recorrer una cadena 2

n = int(input())
for i in range(0, n):
    cadena = input()
    new_cadena = ""
    for c in cadena:
        new_cadena += c + ","
    print(new_cadena[0:len(new_cadena)-1])