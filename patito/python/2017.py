# Problem ID: 2017
# Title: Ej_vector

n = int(input())
v = []
pares = []
for i in range(0, n):
    e = int(input())
    if e % 2 == 0:
        pares.append(e)
    else:
        v.append(e)
pares.sort()
print(*pares, sep="\n")
print("")
s = ",".join(map(str,v))
print("{},".format(s))