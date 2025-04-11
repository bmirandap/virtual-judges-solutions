# Problem ID: 1333
# Title: Easy Suffix Array

s = input()
n = len(s)
cad = []
for i in range(0, n):
    cad.append(s[i:n+1])
cad.sort()
for c in cad:
    print(c)