"""
Ch 8 Question 4 - Random Turtle Walk
---
Edward Naidoo
BSYS-2065
April 25, 2023
"""

import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()

wn.bgcolor('lightgreen')
t.color('lightpink')
angles = []

for i in range(10):
    angles.append(random.randint(0, 360))

def main():
    for a in angles:
        # t.right(angle)
        t.forward(50)
        t.left(a)
        t.forward(50)
        t.right(a)

if __name__ == "__main__":
    main()

turtle.mainloop()