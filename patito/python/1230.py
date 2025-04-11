# Problem ID: 1230
# Title: Descomponer el tiempo

n = int(input())
horas = 0
minutos = 0
segundos = 0
while n >= 3600:
    horas += 1
    n -= 3600
while n >= 60:
    minutos += 1
    n -= 60
segundos = n
print("{} {} {}".format(horas, minutos, segundos))