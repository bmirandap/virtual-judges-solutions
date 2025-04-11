# Problem ID: 1233
# Title: Bob y los parentesis

def verifica(cadena):
    pila = []
    simbolos = {'(': ')', '[': ']'}
    for c in cadena:
        if c in simbolos:
            pila.append(c)
        elif len(pila) == 0 or c != simbolos[pila.pop()]:
            return False
    return len(pila) == 0    
        
n = int(input())
for i in range(0,n):
    cadena = input()
    auxcad = ""
    for c in cadena:
        if c != ' ':
           auxcad += c 
    print("Yes" if verifica(auxcad) else "No")