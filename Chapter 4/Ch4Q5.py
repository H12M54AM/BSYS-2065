import turtle

t1 = turtle.Turtle()
t1.color("red")

t2 = turtle.Turtle()
t2.color("orange")

t3 = turtle.Turtle()
t3.color("yellow")

t4 = turtle.Turtle()
t4.color("green")

# Equilateral Triangle
for i in range(3):
    t1.forward(100)
    t1.left(120)
    
# Square
t2.right(180)
for i in range(4):
    t2.forward(100)
    t2.right(90)
    
# Hexagon
t3.left(90)
for i in range(6):
    t3.right(60)
    t3.forward(100)
    
# Octagon
t4.right(90)
for i in range(8):
    t4.right(45)
    t4.forward(50)

turtle.mainloop()