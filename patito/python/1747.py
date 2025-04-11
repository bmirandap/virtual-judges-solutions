# Problem ID: 1747
# Title: Medidas Estadísticas

import sys
from queue import PriorityQueue
def respuesta(cp):
    array = []
    while not cp.empty():
        array.append(cp.get())
    for e in array:
        cp.put(e)
    if cp.empty():
        print("sin elementos")
    else:
        print("minimo: {} maximo: {} promedio {:.4f}".format(min(array), max(array), (sum(array)/len(array))))

cp = PriorityQueue()
for lista in sys.stdin:
    if lista == "\n":
        break
    lista = lista[0: len(lista)-1]
    if "numero" in lista:
        cp.put(int(lista.split()[1]))
        respuesta(cp)
    else:
        if cp.empty():
            print("sin elementos")
        else:
            cp.get()
            respuesta(cp)
   