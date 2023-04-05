"""
Ch 6 Question 1 - Squares
---
Edward Naidoo
BSYS-2065
April 5, 2023
"""
import turtle

wn = turtle.Screen()
t = turtle.Turtle()

tcolour = "pink"
wn.setworldcoordinates(-100, -100, 800, 800)

# Square
def square(ttl, sz):
    """
    Square\n
    ttl = turtle object, sz = size
    """
    for i in range(4):
        ttl.forward(sz)
        ttl.left(90)

def space(ttl, len):
    """
    Adds space between squares\n
    ttl = turtle object, len = length
    """
    ttl.penup()
    ttl.forward(len)
    ttl.pendown()

def main():
    wn.bgcolor("lightgreen")
    t.pensize(5)
    t.color(tcolour)
    square(t, 100)
    space(t, 150)
    square(t, 100)
    space(t, 150)
    square(t, 100)
    space(t, 150)
    square(t, 100)
    space(t, 150)
    square(t, 100)
    space(t, 150)

if __name__ == '__main__':
    main()

turtle.mainloop()