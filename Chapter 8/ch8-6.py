"""
Ch 8 Question 6 - If turtle goes to border, it will turn around
---
Edward Naidoo
BSYS-2065
May 2, 2023
"""

import turtle
import random

# Objects
t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

# Settings
wn.bgcolor('lightgreen')
t1.color('darkblue')

def moveRandom(t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(random.randrange(0, 360))
    else:
        t.right(random.randrange(0, 360))

    t.forward(50)

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        t.left(180)
    if turtleY > topBound or turtleY < bottomBound:
        t.left(180)
    return stillIn

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

t1.up()
t1.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()

while isInScreen(wn, t1) and isInScreen(wn, t2) and not areColliding(t1, t2):
    moveRandom(t1)
    moveRandom(t2)
    if areColliding(t1, t2):
        t1.right(180)
        t2.right(180)

turtle.mainloop()