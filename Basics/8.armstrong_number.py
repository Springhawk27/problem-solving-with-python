#   Armstrong Number
""" 
A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if,
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

"""


def checkArmstrong(num):

    if num in range(1, 10):
        return True

    order = len(str(num))
    sum = 0

    number = num

    while num > 0:
        digit = num % 10
        sum += digit ** order
        num = num // 10

    if sum == number:
        return True
    return False


n = int(input("Enter any positive number: "))

if checkArmstrong(n):
    print("Number is Armstrong")
else:
    print("Number is not armstrong")
