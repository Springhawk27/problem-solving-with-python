#  compound interest

""" 
Formula:
A = P(1 + r/100)^t
Compound Interest = A - P 
Where, 
A - Amount, P - Principle amount, r - rate, t - time
"""


def compoundInterest(principle, time, rate):
    amount = principle * (pow((1+rate/100), time))
    ci = amount - principle
    return ci


p = 15000
t = 5
r = 9.5

result = compoundInterest(p, t, r)
print("Compound Interest is {:.3f}".format(result))
