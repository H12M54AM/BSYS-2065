"""
Ch 7 Question 13 - Easter Dates
---
Edward Naidoo
BSYS-2065
April 25, 2023
"""

def date_of_easter(year:int):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e

    if year >= 1900 and year <= 2099:
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            dateofeaster -= 7

        if dateofeaster > 31:
            print(f"April {abs(dateofeaster-31)}") 
        else:
            print(f"March {abs(dateofeaster)}") 

    else:
        print("Year out of range...")

user = int(input("what year?: "))
date_of_easter(user)