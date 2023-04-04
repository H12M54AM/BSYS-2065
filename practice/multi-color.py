import turtle
import Shapes

ct = turtle.Turtle()
s = Shapes.Shapes()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Large Colourful Snow Flake
for c in colors:
    ct.color(c)
    ct.forward(100)
    ct.right(360/(len(colors)+1))
    ct.backward(100)

# Displacement
ct.right(180)
ct.penup()
ct.forward(120)
ct.pendown()

# Spiral
max_num = 100
count = 0
for i in range(max_num):
    ct.left(50)
    ct.forward(i)

s.displacement(ct, 90, 0)
s.tiny_snowflake(ct, 90)

s.displacement(ct, 120, 0)
s.tiny_snowflake(ct, 50)

s.displacement(ct, 110, 0)
s.tiny_snowflake(ct, 40)

s.displacement(ct, 130, 0)
s.tiny_snowflake(ct, 80)

s.displacement(ct, 50, 1)
s.tiny_snowflake(ct, 250)

turtle.mainloop()