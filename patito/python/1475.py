# Problem ID: 1475
# Title: Invertir un rango

n,i,j = map(int, input().split())
a = list(map(int, input().split()))
a = a[0:n]
aux = a[i:j+1]
aux = aux[::-1]
anew = []
anew.extend(a[0:i])
anew.extend(aux)
anew.extend(a[j+1:n])
for i in range(0, n):
    print(anew[i])