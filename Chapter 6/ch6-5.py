"""
Ch 6 Question 5 - Double Spirals
---
Edward Naidoo
BSYS-2065
April 9, 2023
"""
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

straight = turtle.Turtle()
spiral = turtle.Turtle()

straight.pencolor("blue")
spiral.pencolor("blue")

def maze_square(ttl):
    increment = 0
    ttl.penup()

    ttl.right(180)
    ttl.forward(140)
    ttl.right(180)

    ttl.pendown()    
    for i in range(100):
        increment += 2
        ttl.right(90)
        ttl.forward(increment)
    

def spiral_square(ttl):
    inc_forward = 0
    inc_degrees = 0
    ttl.penup()
    ttl.forward(140)
    ttl.pendown()

    for i in range(100):
        inc_forward += 2
        ttl.right(90 + inc_degrees)
        inc_degrees -= 0.01
        ttl.forward(inc_forward)

def main():
    maze_square(straight)
    spiral_square(spiral)

if __name__ == '__main__':
    main()

turtle.mainloop()