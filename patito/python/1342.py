# Problem ID: 1342
# Title: Fibonacci Modular

def fibo(n):
    tabla = []
    tabla.append(0)
    tabla.append(1)
    for i in range(2, n+1):
        tabla.append(tabla[i-1] + tabla[i-2])
    return tabla[n]

t = int(input())
for i in range(0, t):
    m, n = map(int, input().split())
    print(fibo(m) % n)