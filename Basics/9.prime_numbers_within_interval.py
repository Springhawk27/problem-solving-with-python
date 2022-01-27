#  print all Prime numbers in an Interval
""" 
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, 13,..}.
"""


def primeNumbers():
    primeNum = []
    for i in range(1, 20):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                primeNum.append(i)
    return primeNum


result = primeNumbers()
if(len(result) == 0):
    print("There is no prime numbers in the given interval")
else:
    print("The prime numbers in the given interval are {}".format(result))
