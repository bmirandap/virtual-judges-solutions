# Problem ID: 1427
# Title: Tabla de Multiplicar

n = list(range(1,11))
print("uno\tdos\ttres\tcuatro\tcinco\tseis\tsiete\tocho\tnueve\tdiez")
i = 1
while i <= 10:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(n[0]*i, n[1]*i, n[2]*i, n[3]*i, n[4]*i, n[5]*i, n[6]*i, n[7]*i, n[8]*i, n[9]*i))
    i += 1