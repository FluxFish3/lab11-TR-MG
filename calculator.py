"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        print("The value of a must be >= 0.")

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    return math.log(b, a)

def exponent(a, b):
    return a**b


