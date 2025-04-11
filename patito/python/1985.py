
# Problem ID: 1985
# Title: Coronavirus

t = int(input())
for i in range(0, t):
    n = int(input())
    personas = list(map(int, input().split()))
    personas.sort()
    a = []
    b = []
    minimo = 999999999
    division = 0
    for j in range(0,n-1):
        a = personas[0:j+1]
        b = personas[j+1:n]
        minimoaux = abs(max(a) - min(b))
        if minimoaux < minimo:
            minimo = minimoaux
            division = j
    print(abs(max(personas[0:division+1]) - min(personas[division+1:n])))