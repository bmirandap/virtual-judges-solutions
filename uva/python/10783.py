# Problem ID: 10783
# Title: Odd Sum

n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    lista = list(range(a, b + 1))
    s = 0
    for j in lista:
        if j % 2 != 0:
            s += j
    print("Case {}: {}".format(i + 1, s))