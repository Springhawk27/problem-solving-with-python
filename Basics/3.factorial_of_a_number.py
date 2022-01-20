#  factorial of a number
""" 
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.
"""

# built-in function
import math


def fact1(n):
    return math.factorial(n)


y = 4
fact1Result = fact1(y)
print("factorial of {} is {}".format(y, fact1Result))

# Recursive Method and using ternary operator


def fact2(n):
    return 1 if(n == 1 or n == 0) else n*fact2(n-1)


x = 5
fact2Result = fact2(x)
print("factorial of {} is {}".format(x, fact2Result))


# Iterative Method
def fact3(n):
    if(n < 0):
        return 0
    elif(n == 1):
        return 1
    else:
        fact = 1
        while(n > 1):
            fact = fact * n
            n = n - 1
        return fact


z = 6
fact3Result = fact3(z)
print("factorial of {} is {}".format(z, fact3Result))
