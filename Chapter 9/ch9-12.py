"""
Ch 9 Question 12 - Removes Strings from other strings
---
Edward Naidoo
BSYS-2065
May 7, 2023
"""

ori_string = input("Whats the String?: ")
removed_string = input(f"What letters do you want to remove from '{ori_string}': ")

# def remove_all(string:str, substr:str) -> str:
#     return string.replace(substr, '')

def remove_substring(string:str, to_remove:str) -> str:
    """Removes all occurrences of a string from another string."""
    substring_length = len(to_remove)
    i = 0
    while i <= len(string) - substring_length:
        if string[i:i+substring_length] == to_remove:
            string = string[:i] + string[i+substring_length:]
        else:
            i += 1
    return string

print(remove_substring(ori_string, removed_string))