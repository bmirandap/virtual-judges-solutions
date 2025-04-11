# Problem ID: 158A
# Name: Next Round

n, k = map(int, input().split())
scores = list(map(int, input().split()))
c = 0
for i in range(0, n):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        c += 1
    else:
        break
print(c)