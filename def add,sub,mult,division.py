def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    else:
        return a/b
    
num1=5
num2=10

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multipication:", multiply(num1, num2))
print("Division:", divide(num1, num2))