# Problem ID: 1474
# Title: Nuevo vector

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(0,n):
    car = input()
    if car == '+':
        print(a[i] + b[i])
    if car == '*':
        print(a[i] * b[i])
    if car == '>':
        print(a[i] if a[i] > b[i] else b[i])
    if car == '<':
        print(a[i] if a[i] < b[i] else b[i])