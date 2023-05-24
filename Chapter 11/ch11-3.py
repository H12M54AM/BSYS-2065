"""
Ch 11 Question 3 - min max in student data txt
---
Edward Naidoo
BSYS-2065
May 23, 2023
"""
f = open("./data/studentdata.txt", "r")

for aline in f:
    items = aline.split()
    for i in range(len(items[1:])):
        #converting scores from strings to integers
        items[i+1] = int(items[i+1])
    print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))

f.close()
