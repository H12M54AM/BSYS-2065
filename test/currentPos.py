"""
Illustrates displacment within space and plotting accurate
coordinates for better reading.
---
Edward Naidoo
April 26, 2023
"""
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Experiment on Turtle Coordinates")

# Changes current displacement relative to origin (0.0, 0.0)
t.goto(10.0, -30.0)

# Returns change from displacement relative to origin
before = t.pos()

# Movements
for i in range(5):
    t.forward(100)
    t.left(60)

# Returns ending coordinates
after = t.pos()

# Where turtle is
print(f"Current Position {after}")

# The displacemet from origin, not from 'goto' method
print(f"Moved {after-before}px")

turtle.mainloop()