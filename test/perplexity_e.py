import random
import turtle

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)
    if not isInScreen(wn, t):
        t.right(180)

def areColliding(t1, t2):
    if t1.distance(t2) < 20:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2
    turtleX = t.xcor()
    turtleY = t.ycor()
    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
        t.right(180)
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
        t.right(180)
    for other_turtle in turtles:
        if other_turtle != t and areColliding(t, other_turtle):
            stillIn = False
            t.right(180)
    return stillIn

turtles = []
for i in range(5):
    t = turtle.Turtle()
    t.shape('turtle')
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    turtles.append(t)

wn = turtle.Screen()

while True:
    for t in turtles:
        moveRandom(wn, t)