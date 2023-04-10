"""
Ch 6 Question 9 - 5 pointed Star
---
Edward Naidoo
BSYS-2065
April 9, 2023
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()

t.pencolor("blue")
t.backward(50)

def fivePointStar():
    for i in range(5):
        t.forward(100)
        t.left(216)

fivePointStar()

turtle.mainloop()