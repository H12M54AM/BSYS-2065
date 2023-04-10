"""
Ch 6 Question 6 - Equilateral Triangle
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

def drawEquilateral(t):
    for i in range(3):
        t.forward(100)
        t.left(120)

drawEquilateral(t)

turtle.mainloop()