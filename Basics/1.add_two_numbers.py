""" 
Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.
"""

num1 = 20
num2 = 30

sum = num1 + num2

print("Sum of {} and {} is {} ".format(num1, num2, sum))
print("Sum of {1} and {0} is {2} ".format(num1, num2, sum))


# using user prompt

num1 = input("Enter the first number: ")
num2 = input("Enter the first number: ")

sum = float(num1) + float(num2)

print("Sum of {} and {} is {} ".format(num1, num2, sum))
