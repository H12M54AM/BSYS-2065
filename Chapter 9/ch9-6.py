"""
Ch 9 Question 6 - Reverse String
---
Edward Naidoo
BSYS-2065
May 7, 2023
"""

userS = input("Input a string: ")

def reverse(word:str) -> str:
    newW = ''
    for i in word:
        newW = i + newW
        
    return newW

print(reverse(userS))