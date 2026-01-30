def add(a, b, c=0):
    return a + b + c

def sub(a, b, c=0):
    return a - b - c

def mul(a, b, c=1):
    return a * b * c

def div(a, b, c=1):
    return (a / b) / c

print(add(1, 2))        
print(add(1, 2, 5))     
print()

print(sub(5, 3))        
print(sub(5, 3, 1))     
print()

print(mul(2, 5))        
print(mul(2, 5, 5))     
print()

print(div(10, 5))       
print(div(10, 5, 2))
