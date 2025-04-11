# Problem ID: 1157
# Title: SO

from queue import PriorityQueue
cp = PriorityQueue()
t = int(input())
for i in range(0,t):
    n = int(input())
    salida = ""
    for j in range(0,n):
        entrada = input()
        if entrada[0] == 'I':
            cp.put(int(entrada[2]))
        if entrada[0] == 'E':
            salida += str(cp.get()) + " "
    if len(salida) > 0:
        print(salida[0:len(salida)-1])