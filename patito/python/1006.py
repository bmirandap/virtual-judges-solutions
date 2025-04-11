# Problem ID: 1006
# Title: Cadena Bailarina

t = int(input())
for i in range(0, t):
    cadena = input()
    new_cadena = ""
    may = True
    for c in cadena:
        if c == ' ':
            new_cadena += ' '
        else:
            new_cadena += c.upper() if may else c.lower()
            may = not may
    print(new_cadena)