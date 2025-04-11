# Problem ID: 2055
# Title: K- esimo no divisible por n

t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = 1
    b = n*k
    if k < n:
        print(k)
    else:
        while (b-a) > 1:
            medio = (a + b) // 2            
            if (medio - (medio // n)) >= k:
                b = medio
            else:
                a = medio
        print(b)