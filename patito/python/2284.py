# Problem ID: 2284
# Title: Reto1

a = int(input())
b = int(input())
c = int(input())

def mayor(x, y):
    return x if x > y else y
    
print(mayor(a, mayor(b, c)))