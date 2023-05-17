"""
Ch 10 Question 12 - Count till 'Sam'
---
Edward Naidoo
BSYS-2065
May 16, 2023
"""
names = ['Jaime', 'Dan', 'Ken', 'Edward', 'Sam', 'Alen', 'Don']

def count_names(nm:list) -> int:
    """Takes a List and counts up unit it reaches 'sam'"""
    count = 0
    for i in nm:
        if i.lower() != 'sam':
            count += 1
        else:
            break
    
    return count

print(count_names(names))