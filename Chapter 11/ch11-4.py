"""
Ch 11 Question 4 - lab data in turtle
---
Edward Naidoo
BSYS-2065
May 23, 2023
"""

import turtle

# backend
temp = []
coords = []
with open("./data/labdata.txt", "r") as data:
    for i in data:
        # items = i.split()
        # grades = items[1:]
        # int_grades = [int(i) for i in grades]
        temp = i.split()
        # temp = pairs
        coords.append(int(temp))

# frontend
t = turtle.Turtle()
wn = turtle.Screen()

def main():
    print(coords)

if __name__ == '__main__':
    main()

turtle.mainloop()