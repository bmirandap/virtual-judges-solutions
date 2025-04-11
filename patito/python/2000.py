# Problem ID: 2000
# Title: Días de salida

t = int(input())
for i in range(0,t):
    x1, x2, x3 = map(int, input().split())
    num = []
    num.append(x1)
    num.append(x2)
    num.append(x3)
    num.sort()
    print((num[1]-num[0]) + (num[2]-num[1]))