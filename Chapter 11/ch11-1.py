"""
Ch 11 Question 1 - student data txt
---
Edward Naidoo
BSYS-2065
May 23, 2023
"""
with open('./data/studentdata.txt', 'r') as data:
    for i in data:
        items = i.split()
        if len(items[1:]) > 6:
            print(items[0])