# Problem ID: 1019
# Title: Reduciendo Costos

t = int(input())
for i in range(1,t+1):
    salarios = list(map(int, input().split()))
    salarios.sort()
    print("Case {}: {}".format(i, salarios[1]))