"""
Ch 7 Question 6 - findHypot Function
---
Edward Naidoo
BSYS-2065
April 24, 2023
"""

import math

def findHypot(x:float, y:float) -> float:
    return math.sqrt(x*x + y*y)

x = float(input("What is x: "))
y = float(input("What is y: "))

print(findHypot(x, y))