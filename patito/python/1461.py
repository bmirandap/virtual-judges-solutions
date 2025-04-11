# Problem ID: 1461
# Title: Números Felices

def es_feliz(num):
    r = num
    suma_cuadrados = []
    while True:
        if r == 1:
            return True
        r = sum(int(d) ** 2 for d in str(r))
        if r in suma_cuadrados:
            return False
        suma_cuadrados.append(r)
        
n = int(input())
for i in range(0,n):
    num = int(input())
    if es_feliz(num):
        print("Feliz")
    else:
        print("Triste")