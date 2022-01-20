#  find area of a circle
""" 
Area = pi * r2
where r is radius of circle 
"""


def area(r):
    pi = 3.1416
    return pi * (r*r)


r = 4
result = area(r)
print("Area of radius {} is {:.5f}".format(r, result))
print("Area of radius %s  is %.5f" % (r, result))
