# Problem ID: 1059
# Title: intersección

a, b = map(int, input().split())
listaA = list(map(int, input().split()))
listaB = list(map(int, input().split()))
setA = set(listaA[0:a])
setB = set(listaB[0:b])
print(len(setA&setB))