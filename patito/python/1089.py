# Problem ID: 1089
# Title: Epicentro

n = input()
if len(n) % 2 == 0:
    print("*")
elif len(n) > 1:
    print(n[(len(n)//2)])
else:
    print(n[0])