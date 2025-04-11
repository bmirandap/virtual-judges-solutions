# Problem ID: 1043
# Title: Crafting in Minecraft

n = int(input())
for i in range(0, n):
    r, p = map(int, input().split()) 
    c = 0
    while r >= 3 and p >= 2:
        c += 1
        r -= 3
        p -= 2
    print("{} {}".format(c, r+p))