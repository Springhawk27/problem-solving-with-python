#  whether a number is Prime or not
""" 
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.
"""

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print("{} is not a prime number".format(number))
            break
    else:
        print("{} is a prime number".format(number))

else:
    print("{} is not a prime number".format(number))
