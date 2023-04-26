"""
Ch 8 Question 5 - Random Turtle Walk from Starting Location
---
Edward Naidoo
BSYS-2065
April 26, 2023
"""

import turtle
import random

class Movements:
    def __init__(self):
        pass
    
    def isInView(ttl):
        """
        Checks if the Turtle is in the
        viewport\n
        returns true, false\n
        """
        pass









# Objects
t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

# Settings
wn.bgcolor('lightgreen')
t1.color('lightpink')
t2.color('blue')

x = random.randint(-100, 100)
y = random.randint(-100, 100)

# Coordinates/Positioning
t1.goto(x, y)
t2.goto(x, y)
position1_bef = t1.pos()
position2_bef = t2.pos()

height = wn.window_height()
width = wn.window_width()

# Random Angles
angles1 = []
angles2 = []

for i in range(10):
    angles1.append(random.randint(0, 360))

for i in range(10):
    angles2.append(random.randint(0, 360))

# Functions
def main():
    while position1_bef < width and position1_bef < height:
        for a in angles1:
            t1.forward(50)
            t1.left(a)
            t1.forward(50)
            t1.right(a)
    position1_aft = t1.pos()
    print(position1_aft)
    while position2_bef < width and position2_bef < height:
        for a in angles2:
            t2.forward(50)
            t2.left(a)
            t2.forward(50)
            t2.right(a)
    position2_aft = t2.pos()
    print(position2_aft)

if __name__ == "__main__":
    main()

turtle.mainloop()