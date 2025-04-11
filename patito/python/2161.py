# Problem ID: 2161
# Title: Cuadrado o Reactangulo

a, b, c = map(int, input().split())
if a * a == b * c:
    print("ambos")
elif a * a > b * c:
    print("cuadrado")
else:
    print("rectangulo")