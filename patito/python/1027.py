# Problem ID: 1027
# Title: INFIX

def operacion(array, ope):
    r = 0
    if ope == 'S':
        r = int(array[0]) + int(array[1])
    if ope == 'R':
        r = int(array[0]) - int(array[1])
    if ope == 'M':
        r = int(array[0]) * int(array[1])
    if ope == 'D':
        aux = []
        aux.append(int(array[0]))
        aux.append(int(array[1]))
        aux.sort(reverse=True)
        r = aux[0] // aux[1]
    if ope == 'C':
        r = int(array[0]) ** 2
    return str(r)

n = int(input())
for i in range(0, n):
    array = input().split()
    aux = []
    t = len(array)
    for j in range(0, t):
        if array[j] != 'S' and array[j] != 'R' and array[j] != 'M' and array[j] != 'D' and array[j] != 'C':
            aux.append(array[j])
        else:
            if j == t-1:
                print(operacion(aux, array[j]))
                aux = []
            else:
                r = operacion(aux, array[j])
                aux = []
                aux.append(r)
if len(aux) > 0:
    print(aux[0])