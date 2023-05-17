"""
Ch 10 Question 4 - Gives Average
---
Edward Naidoo
BSYS-2065
May 16, 2023
"""
list_of_nums = [2, 34, 1, 56, 3, 67, 3, 24]
def avg(numbers:float) -> float:
    total = 0
    for i in numbers:
        total += i
    return total/len(numbers)

print(avg(list_of_nums))

