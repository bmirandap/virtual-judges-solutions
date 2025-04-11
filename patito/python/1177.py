# Problem ID: 1177
# Title: Multisuma

def operaciones(p, operador):
    p_copy = p.copy()
    p_aux = []
    operacion = False
    while len(p_copy) > 0:
        e = p_copy.pop()
        if e == operador:
            operacion = True
        elif operacion:
            if operador == '*':
                p_aux.append(str(int(p_aux.pop()) * int(e)))
            if operador == '+':
                p_aux.append(str(int(p_aux.pop()) + int(e)))
            operacion = False
        else:
            p_aux.append(e)
    return p_aux
    
def maximo(p):
    return (operaciones(operaciones(p,'+'), '*').pop())

def minimo(p):
    return (operaciones(operaciones(p,'*'), '+').pop())

n = int(input())
for i in range(0, n):
    array = list(input())
    t = len(array)
    pila = []
    s = ""
    for j in range(0, t):
        if array[j] == '+' or array[j] == '*':
            pila.append(s)
            pila.append(array[j])
            s = ""
        else:
            s += array[j]
    pila.append(s)
    print("El maximo y minimo son {} y {}.".format(maximo(pila), minimo(pila)))