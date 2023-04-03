import turtle
t = turtle.Turtle()

data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for d in data:
    t.forward(100)
    t.left(d)
    t.forward(100)
    t.left(d)
    
