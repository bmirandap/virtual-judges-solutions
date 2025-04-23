# Problem ID: 11879
# Title: Multiple of 17

while True:
    x = int(input())
    if x == 0:
        break
    if x % 17 == 0:
        print(1)
    else:
        print(0)