#https://github.com/FluxFish3/lab11-TR-MG
#Partner 1: Michael Galiani
#Partner 2: Tomas Ramirez


# First example
import math

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        print("The value of a must be >= 0")

def hypotenuse(a, b):
    math.hypot(a, b)

# First example
def add(a, b):
   return a + b


def sub(a, b):
   return a - b


def mul(a, b):
   return a * b


def div(a, b):
   if a == 0:
       raise ZeroDivisionError()
   return b / a


def log(a, b):
   if a < 0 or a == 1:
       raise ValueError()
   if b <= 0:
       raise ValueError()
   return math.log(a, b)

def exp(a, b):
   return a**b


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    return math.log(b, a)

def exponent(a, b):
    return a**b


