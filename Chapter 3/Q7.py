# Needs work
"""
Write a Python program that assigns the principal amount 
of 10000 to variable P, assign to n the value 12, and 
assign to r the interest rate of 8% (0.08). Then have 
the program prompt the user for the number of years, t, 
that the money will be compounded for. Calculate and 
print the final amount after t years.
"""

P = 10000
n = 12.0
r = 0.08
t = float(input("How many years?: "))

print(f"The final amount is: ${(P * (1.0 + (r/n)))**n*t}")