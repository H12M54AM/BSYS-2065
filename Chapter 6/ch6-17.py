"""
Ch 6 Question 17 - Fancy Squares
---
Edward Naidoo
BSYS-2065
April 11, 2023
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()

def triangle(ttl):
    for i in range(3):
        ttl.forward(10)
        ttl.left(120)

def drawSprite(ttl, legs, len):
    """
    Draws a Sprite based off of user arguments
    ttl = turtle object\n
    legs = number of legs\n
    len = length of legs\n
    """
    for i in range(legs):
        ttl.pendown()
        ttl.forward(len)
        triangle(ttl)
        ttl.penup()
        ttl.backward(len)
        ttl.pendown()
        ttl.right(360/legs)

def fancySquare(ttl):
    size = 150
    ttl.penup()
    ttl.goto(-size/2, -size/2)
    ttl.pendown()
    
    for i in range(4):
        ttl.forward(size)
        drawSprite(ttl, 15, 20)
        ttl.left(90)

def main():
    fancySquare(t)
    # drawSprite(t, 15, 100)

if __name__ == '__main__':
    main()

turtle.mainloop()