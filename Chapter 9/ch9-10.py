"""
Ch 9 Question 10 - Counts Non-overlaping occurances in substring
---
Edward Naidoo
BSYS-2065
May 7, 2023
"""

userS = input("Input a string: ")
subStr = input("Input a string to count: ")

def count_occur(word:str, substr:str):
    count = 0
    for i in word:
        if substr == i:
            count += 1
    return count

print(count_occur(userS, subStr))