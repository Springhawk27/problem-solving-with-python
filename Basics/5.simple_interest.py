#  simple interest
""" 
Formula:
Simple Interest = (P x T x R)/100
Where, P - principle amount, T - time and, R - rate.
"""


def simpleInterest(p, t, r):

    si = (p*t*r)/100
    return si


p = 15000
t = 5
r = 9.5
result = simpleInterest(p, t, r)
print("Simple Interest is {:.2f}".format(result))
