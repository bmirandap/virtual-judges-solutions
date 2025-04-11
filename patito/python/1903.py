# Problem ID: 1903
# Title: Preguntar si una subcadena existe

n = int(input())
for i in range(0, n):
    cadena = input()
    subcadena = input()
    print("si" if subcadena in cadena else "no")