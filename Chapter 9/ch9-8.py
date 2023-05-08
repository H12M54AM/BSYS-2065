"""
Ch 9 Question 8 - Removes Mode of String
---
Edward Naidoo
BSYS-2065
May 7, 2023
"""

userS = input("Enter a String: ")
Letter = input("Enter a Letter to Remove: ")

def remove_letter(word:str, letter:str) -> str:
    newW = ''
    for w in word:
        if not letter in w:
            newW += w
        
    return newW

print(remove_letter(userS, Letter))