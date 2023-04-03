"""
Ch 4 Question 4 - num and product of num
-----
Write a loop that prints each of the numbers on a new line.
Write a loop that prints each number and its square on a new line.
---
Edward Naidoo
BSYS-2065
March 2023
"""
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in numbers:
    print(num)
    
for num in numbers:
    print(f"{num} = {num**2}")