# Problem ID: 231A
# Name: Team

n = int(input())
cont = 0
for i in range(0, n):
    line = input()
    c = 0
    for num in line:
        if num == "1":
            c += 1
    if c > 1:
        cont += 1
print(cont)