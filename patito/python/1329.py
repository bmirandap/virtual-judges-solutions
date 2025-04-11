# Problem ID: 1329
# Title: Ordenando en rango

n,i,j = map(int, input().split())
a = list(map(int, input().split()))
a = a[0:n]
aux = a[i:j+1]
aux.sort()
anew = []
anew.extend(a[0:i])
anew.extend(aux)
anew.extend(a[j+1:n])
s = ""
for i in range(0,n):
    s += str(anew[i]) + " "
s = s.rstrip()
print(s)