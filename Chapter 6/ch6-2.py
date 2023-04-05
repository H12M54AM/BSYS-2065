"""
Ch 6 Question 2 - multi-square
---
Edward Naidoo
BSYS-2065
April 5, 2023
"""
import turtle

wn = turtle.Screen()
t = turtle.Turtle()

tcolour = "pink"

# Square
def square(t):
    """
    Makes square within square
    """
    size = 20
    for i in range(5):
        t.penup()
        t.goto(-size/2, -size/2)
        t.pendown()
        for j in range(4):
            t.forward(size)
            t.left(90)
        size += 20

def main():
    wn.bgcolor("lightgreen")
    t.pensize(3)
    t.color(tcolour)
    square(t)
     

if __name__ == '__main__':
    main()

turtle.mainloop()