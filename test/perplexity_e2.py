import random
import turtle

def is_in_screen(w, t):
    left_bound = -w.window_width() / 2
    right_bound = w.window_width() / 2
    top_bound = w.window_height() / 2
    bottom_bound = -w.window_height() / 2
    turtle_x, turtle_y = t.position()
    return left_bound < turtle_x < right_bound and bottom_bound < turtle_y < top_bound

def are_colliding(t1, t2, distance):
    turtle1_x, turtle1_y = t1.position()
    turtle2_x, turtle2_y = t2.position()
    distance_between = ((turtle1_x - turtle2_x) ** 2 + (turtle1_y - turtle2_y) ** 2) ** 0.5
    return distance_between < distance

turtles = []
colors = ['red', 'blue']
for i in range(2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(colors[i])
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    turtles.append(t)

wn = turtle.Screen()
wn.bgcolor('white')
wn.title('Turtle Race')

font = ('Arial', 16, 'bold')
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write('Red: 0   Blue: 0', align='center', font=font)

while True:
    for i in range(len(turtles)):
        turtles[i].forward(random.randint(1, 10))
        if not is_in_screen(wn, turtles[i]):
            turtles[i].goto(random.randint(-200, 200), random.randint(-200, 200))
    if are_colliding(turtles, turtles[1], 50):
        turtles.write('Winner!', align='center', font=font)
        turtles[1].write('Winner!', align='center', font=font)
        score_turtle.clear()
        score_turtle.write('Red: 1   Blue: 1', align='center', font=font)
        turtles.goto(-100, 0)
        turtles[1].goto(100, 0)
        turtles.setheading(0)
        turtles[1].setheading(180)
        turtles.pendown()
        turtles[1].pendown()
        turtles.forward(200)
        turtles[1].forward(200)
        turtles.penup()
        turtles[1].penup()
        turtles.goto(random.randint(-200, -100), random.randint(-200, 200))
        turtles[1].goto(random.randint(100, 200), random.randint(-200, 200))
        turtles.setheading(90)
        turtles[1].setheading(90)
        turtles.pendown()
        turtles[1].pendown()
        break

turtle.done()