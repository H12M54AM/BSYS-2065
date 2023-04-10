"""
Ch 6 Question 8 - Area of Circle
---
Edward Naidoo
BSYS-2065
April 9, 2023
"""

import math

def areaOfCircle(r):
    """
    returns area of circle\n
    r = radius
    """
    return math.pi*r**2

area = float(input("What is the Area?: "))
print(areaOfCircle(area))