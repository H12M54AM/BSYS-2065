"""
Ch 7 Question 12 - Leap Year
---
Edward Naidoo
BSYS-2065
April 24, 2023
"""

def isLeap(year:int):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
y = int(input("What is year?: "))
print(isLeap(y))
