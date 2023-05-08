"""
Ch 9 Question 7 - Reverse String and add original string
---
Edward Naidoo
BSYS-2065
May 8, 2023
"""

userS = input("Input a string: ")

def reverse(word:str) -> str:
    newW = ''
    for i in word:
        newW = i + newW
        
    return newW

def mirror(word:str) -> str:
    return word + reverse(word)

print(mirror(userS))