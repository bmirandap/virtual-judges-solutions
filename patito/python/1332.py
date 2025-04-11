# Problem ID: 1332
# Title: Tarea con cadenas

consonantes = "BCDFGHJKLMNPQRSTVWXZ"
cadena = input().upper()
t = len(cadena)
new_cadena = ""
for i in range(0, t):
    if cadena[i] in consonantes:
        new_cadena += "." + cadena[i].lower()
print(new_cadena)