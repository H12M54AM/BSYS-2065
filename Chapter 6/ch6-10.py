"""
Ch 6 Question 10 - 5 pointed Star
---
Edward Naidoo
BSYS-2065
April 9, 2023
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
# wn.setworldcoordinates(-100, -950, 400, 10)

t = turtle.Turtle()

t.pencolor("blue")
t.pensize(3)
t.penup()
t.backward(200)
t.pendown()

def fivePointStar(ttl):
    for i in range(5):
        ttl.forward(100)
        ttl.left(216)

def space(ttl):
    ttl.penup()
    ttl.left(90)
    ttl.forward(100)
    ttl.right(90)
    ttl.forward(100)
    ttl.pendown()

def main():
    # t.left(60)
    for i in range(5):
        fivePointStar(t)
        
        space(t)

if __name__ == '__main__':
    main()

turtle.mainloop()
