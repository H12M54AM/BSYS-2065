"""
Ch 7 Question 8 - isOdd function
---
Edward Naidoo
BSYS-2065
April 24, 2023
"""

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
    
num = int(input("What is n?: "))
print(is_odd(num))
