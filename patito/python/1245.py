# Problem ID: 1245
# Title: De arriba hacia abajo

x, y = map(int, input().split())
may = 0
men = 0
if x > y:
    may = x
    men = y
else:
    may = y
    men = x
while may >= men:
    print(may)
    may -= 1