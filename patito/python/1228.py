# Problem ID: 1228
# Title: Mayusculas y minusculas

char = input()
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if char in mayusculas:
    print(char.lower())    
else:
    print(char.upper())