"""
Ch 6 Question 14 - mySqrt using Newtons Method
---
Edward Naidoo
BSYS-2065
April 11, 2023
"""

def mySqrt(n):
    # Set the initial guess to n/2
    guess = n/2

    # Iterate until the guess is close enough
    while abs(guess**2 - n) > 0.0001:
        guess = (guess + n/guess) / 2

    return guess
print(mySqrt(25))