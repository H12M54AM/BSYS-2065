"""
Ch 4 Question 6 - Shape Size
---
Write a program that asks the user for the number of sides, 
the length of the side, the color, and the fill color of a 
regular polygon. The program should draw the polygon and 
then fill it in.
---
Edward Naidoo
BSYS-2065
March
"""

import turtle

t = turtle.Turtle()

sides = int(input("How many sides? : "))
length = int(input("How long? : "))
colour = input("Whats the colour? : ")
fill = input("Whats the colour fill? : ")

t.color(colour)
t.begin_fill()

for i in range(sides):
    t.forward(length)
    t.left(90)
    t.fillcolor(fill)
    
t.end_fill()
turtle.mainloop()
