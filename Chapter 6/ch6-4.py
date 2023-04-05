"""
Ch 6 Question 4 - Pretty Pattern
---
Edward Naidoo
BSYS-2065
April 5, 2023
"""
import turtle

wn = turtle.Screen()
t = turtle.Turtle()

tcolour = "pink"

def tinySquare(ttl):
    """
    Creates small squares that is replecated
    ttl = turtle object
    """
    for i in range(4):
        ttl.forward(100)
        ttl.left(90)

def largeSquare(ttl): 
    """
    Uses tinySquare function to create a 
    larger square.
    ttl = turtle object
    """
    for s in range(4):
        tinySquare(ttl)
        ttl.left(90)

def main():
    for j in range(10):
        largeSquare(t)
        t.right(20)

if __name__ == '__main__':
    main()

turtle.mainloop()