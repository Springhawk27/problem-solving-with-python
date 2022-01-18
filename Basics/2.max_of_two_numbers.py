""" 
Given two numbers, write a Python code to find the Maximum of these two numbers.
"""


x = 106
y = 12

if(x > y):
    print("X is greater than Y")
else:
    print("Y is greater than X")


# using user prompt

a = input("Enter the first number:")
b = input("Enter the second number:")

if(a > b):
    print("a is greater than b")
elif(a == b):
    print("a is equal to b")
else:
    print("b is greater than a")


#  using defination/function

def max(a, b):
    if(a > b):
        return("a is greater than b")
    elif(a == b):
        return("a is equal to b")
    else:
        return("b is greater than a")


x = input("Enter the first number:")
y = input("Enter the second number:")


print(max(x, y))


# using max() function

a = 12
b = 10
maximum = max(a, b)
print("Largest number of {} and {} is {}".format(a, b, maximum))
