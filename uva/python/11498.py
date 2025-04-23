# Problem ID: 11498
# Title: Division of Nlogonia

while True:
    k = int(input())
    if k == 0:
        break
    m, n = map(int, input().split())
    for i in range(k):
        x, y = map(int,input().split())
        if x == m or y == n:
            print("divisa")
        elif x > m and y > n:
            print("NE")
        elif x > m and y < n:
            print("SE")
        elif x < m and y > n:
            print("NO")
        else:
            print("SO")