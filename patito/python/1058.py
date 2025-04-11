# Problem ID: 1058
# Title: ordenando números

n = int(input())
for i in range(0,n):
    a = int(input())
    num = list(map(int, input().split()))
    num = num[0:a]
    num.sort()
    cadena = ' '.join([str(e) for e in num])
    print(cadena)