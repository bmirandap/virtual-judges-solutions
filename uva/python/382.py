# Problem ID: 382
# Title: Perfection

def sumaDivisores(n):
    s = 0
    for divisor in range(1, (n // 2) + 1):
        if n % divisor == 0:
            s += divisor
    return s

control = False
print("PERFECTION OUTPUT")
while True:
    numeros = list(map(int, input().strip().split()))
    for n in numeros:
        if n == 0:
            control = True
            break
        else:
            s = sumaDivisores(n)
            if s == n:
                estado = "PERFECT"
            elif s < n:
                estado = "DEFICIENT"
            else:
                estado = "ABUNDANT"
            espacios = ' ' * (5 - len(str(n)))
            print("{}{}  {}".format(espacios, n, estado))
    if control:
        break
print("END OF OUTPUT")