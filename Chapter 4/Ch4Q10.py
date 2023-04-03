"""
Ch 4 Question 10 - Turtle Stamp
---
The program creates a circular pattern by alterating between
penup and pendown.
---
Edward Naidoo
BSYS-2065
March 2023
"""

import turtle 

t = turtle.Turtle()

for i in range(12):
    t.penup()
    t.forward(70)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(20)
    t.stamp()
    t.penup()
    t.backward(100)
    t.right(30)

turtle.mainloop()