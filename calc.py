# simple mathematical operations and factorial
def add(x,y):
    return x + y
def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mul(x,y):
    return x * y

def mod(x,y):
    return x % y

def pow(x,y):
    return x ** y
def sqrt(x):
    return sqrt(x)
def fact(x):    
    if x < 0:
        return "Invalid Input"
    else:
        result = 1
        for i in range(1,x+1):
            result *= i
        return result
