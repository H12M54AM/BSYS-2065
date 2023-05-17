"""
Ch 10 Question 8 - Sums up even numbers of a list
---
Edward Naidoo
BSYS-2065
May 16, 2023
"""
list_of_nums = [2, 34, 1, 56, 3, 67, 3, 24]

def sum_evens(numbers:int) -> int:
    odd = 0
    even = 0
    
    for i in numbers:
        if i % 2 == 0:
            even += i 
            # For Debugging/proof
            print(f"i: {i}")
            print(f"Even: {even}")
            print()
        else:
            odd += i
            # For Debugging/proof
            print(f"i: {i}")
            print(f"Odd: {odd}")
            print()

    return even

print(sum_evens(list_of_nums))