# Problem ID: 1477
# Title: Mediana

n, m = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))
setC = list(set(setA).union(set(setB)))
setC.sort()
print(*setC, sep="\n")