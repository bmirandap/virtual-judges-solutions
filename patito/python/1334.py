# Problem ID: 1334
# Title : Ordenando funciones

def sumaDigitos(n):
    m = n
    s = 0
    while m != 0:
        d = m % 10
        m //= 10
        s += d
    return s

# Modificado
def bubbleSort(array):
    n = len(array)
    for i in range(2, n + 1):
        for j in range(0, n - i + 1):
            if sumaDigitos(array[j]) == sumaDigitos(array[j + 1]):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            else:
                if sumaDigitos(array[j]) > sumaDigitos(array[j + 1]):
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

n = int(input())
lista = list(map(int, input().split()))
lista = lista[0: n]
bubbleSort(lista)
arr = list(map(str, lista))
s = " ".join(arr)
print(s)