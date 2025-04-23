# Problem ID: 11727
# Title: Cost Cutting

n = int(input())
for i in range(n):
    lista = list(map(int, input().split()))
    lista.sort()
    print("Case {}: {}".format(i + 1, lista[1]))