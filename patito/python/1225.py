# Problem ID: 1225
# Title: Máximo de tres números

a, b, c = map(int, input().split())
if a > b:
    print(a if a > c else c)
else:
    print(b if b > c else c)