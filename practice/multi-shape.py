"""
Multi-shape
To practice more using the turtle module
April 4, 2023
BSYS-2065
"""
import turtle
import Shapes

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
other = turtle.Turtle()
s = Shapes.Shapes()

t1.color("red")
t2.color("green")
t3.color("purple")

data = []
forward = int(input("How forward?: "))
choice = int(input("Left or Right (1 or 0): "))

# Square
s.square(t1, forward, choice)

# triangle
s.triangle(t3, forward, choice)

turtle.mainloop()