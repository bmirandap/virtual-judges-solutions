# Problem ID: 1090
# Title: SUMA3

n = int(input())
if n < 4: 
    print("0")
else:
    lista = list(range(3, n, 3))
    print(sum(lista))