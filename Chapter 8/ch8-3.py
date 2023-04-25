"""
Ch 8 Question 3 - is_Prime Function
---
Edward Naidoo
BSYS-2065
April 24, 2023
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True