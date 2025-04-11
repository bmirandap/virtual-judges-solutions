# Problem ID: 1315
# Title: Anti-Acumulada

n = int(input())
array = list(map(int, input().split()))
array = array[0:n]
t = len(array)
s = 0
anti = ""
for i in range(0, t):
    anti += str(array[i] - s) + " " 
    s = array[i]
anti.rstrip()
print(anti)