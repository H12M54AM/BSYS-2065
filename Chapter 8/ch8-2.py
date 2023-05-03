"""
Ch 8 Question 2 - triangular numbers
---
Edward Naidoo
BSYS-2065
April 25, 2023
"""

def triangluar_num(n:int):
    # answer
    counter = 0
    while counter < n:
        counter += 1
        ans = (counter*(counter+1)/2)
        print(counter, ans)

triangluar_num(5)
