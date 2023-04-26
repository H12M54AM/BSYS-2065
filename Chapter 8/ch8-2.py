"""
Ch 8 Question 2 - triangular numbers
---
Edward Naidoo
BSYS-2065
April 25, 2023
"""

# Tn = n(n+1)/2

# Psuedocode
# Get user input
# Create function
    # while ans > 0 or ans < num:
        # print num, ans
# user = int(input("What is the number?: "))

def triangluar_num(n:int):
    # answer
    counter = 0
    while counter < n:
        counter += 1
        ans = (counter*(counter+1)/2)
        print(counter, ans)

triangluar_num(5)
