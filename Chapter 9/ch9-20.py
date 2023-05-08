"""
Ch 9 Question 20 - Remove Duplicate chars in String
---
Edward Naidoo
BSYS-2065
May 7, 2023
"""

string = input("Whats the String?: ")

def remove_dups(string):
    new_string = ''
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

print(remove_dups(string))