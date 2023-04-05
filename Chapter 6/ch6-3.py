"""
Ch 6 Question 3 - Poly Function
---
Edward Naidoo
BSYS-2065
April 5, 2023
"""
import turtle

wn = turtle.Screen()
t = turtle.Turtle()

tcolour = "pink"

def drawPoly(ttl, sides, size):
    """
    Draws a shape based off of 3 parameter\n
    ttl = turtle object.\n
    sides = how many sides in shape?\n
    size = how long each side be?\n
    """
    for i in range(sides):
        ttl.left(45)
        ttl.forward(size)

def main():
    wn.bgcolor("lightgreen")
    t.pensize(3)
    t.color(tcolour)
    drawPoly(t, 8, 50)

if __name__ == '__main__':
    main()

turtle.mainloop()