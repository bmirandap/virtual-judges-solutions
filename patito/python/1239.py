# Problem ID: 1239
# Title: Chat

def ordenacion_burbuja(vec, vec2):
    n = len(vec)
    for i in range(1, n):
        for j in range(0, n-i):
            if vec[j] < vec[j+1]:
                aux = vec[j]
                aux2 = vec2[j]
                vec[j] = vec[j+1]
                vec2[j] = vec2[j+1]
                vec[j+1] = aux
                vec2[j+1] = aux2

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cuenta_letras = [0] * len(letras)

n = int(input())
pos = 0
for i in range(0, n):
    cadena = input()
    for c in cadena:
        if c in letras:
            pos = letras.index(c)
            cuenta_letras[pos] += 1

nuevo_letras = []
nuevo_cuenta_letras = []    
for i in range(0, len(letras)):
    if cuenta_letras[i] != 0:
        nuevo_letras.append(letras[i])
        nuevo_cuenta_letras.append(cuenta_letras[i])

ordenacion_burbuja(nuevo_cuenta_letras, nuevo_letras)
for i in range(0, len(nuevo_letras)):
    print("{} {}".format(nuevo_letras[i], nuevo_cuenta_letras[i]))
