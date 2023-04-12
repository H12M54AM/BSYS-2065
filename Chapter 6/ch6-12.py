"""
Ch 6 Question 12 - Sprite Function
---
Edward Naidoo
BSYS-2065
April 11, 2023
"""
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()

def drawSprite(ttl, legs, len):
    """
    Draws a Sprite based off of user arguments
    ttl = turtle object\n
    legs = number of legs\n
    len = length of legs\n
    """
    for i in range(legs):
        ttl.forward(len)
        ttl.pendown()
        ttl.penup()
        ttl.backward(len)
        ttl.pendown()
        ttl.right(360/legs)
        
def main():
    drawSprite(t, 15, 120)

if __name__ == '__main__':
    main()

turtle.mainloop()