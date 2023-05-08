"""
Ch 9 Question 1 - Childrens Book Error 'Ouack, Quack' 
---
Edward Naidoo
BSYS-2065
May 4, 2023
"""

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)
    if p in  'O':
        p = 'O' + p[:1]
        
    elif p == 'Q':
        p = 'Q' + p[:1]
        


