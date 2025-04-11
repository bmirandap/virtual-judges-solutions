# Problem ID: 1611
# Title: Botones

n, m = map(int, input().split())
lista = list(map(int, input().split()))
lista = lista[0:n]
botones = {}
botones[0] = 'P'
pos = 0
flag = False
for i in range(1, n):
    botones[i] = 'A'

while True:
    if botones[lista[pos]].count('P') > 1:
        break
    else:
        botones[lista[pos]] += 'P'
        botones[pos] += 'A'
        pos = lista[pos]
        
    if botones[m] == "AP" or m == 0:
        flag = True
        break
if flag:
    print("SI")
else:
    print("NO")