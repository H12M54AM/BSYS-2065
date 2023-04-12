"""
Ch 6 Question 18 - Bar Chart
---
Edward Naidoo
BSYS-2065
April 11, 2023
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0, 0, 500, 500)

t = turtle.Turtle()

data = [44, 148, 63, 120, 107, 50, 141, 13, 141, 140]
width = 20

def drawBar(numbers):
    t.forward(10)
    for d in range(len(numbers)):
        t.left(90)
        t.forward(d)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(-d)
        
def barChart(data):
    drawBar(data)
    
def main():
    barChart(data)

if __name__ == '__main__':
    main()

turtle.mainloop()
