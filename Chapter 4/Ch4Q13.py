"""
Ch 4 Question 13 - Sprite Legs
---
Creates a sprite with the number of legs set to the user
---
Edward Naidoo
BSYS-2065
March 2023
"""

import turtle 

t = turtle.Turtle()
legs = int(input("How many legs?: "))

for l in range(legs):
    t.forward(100)
    t.pendown()
    t.stamp()
    t.backward(100)
    t.right(360/legs)

turtle.mainloop()