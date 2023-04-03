import turtle 

t = turtle.Turtle()

# Donut Flower
def donut():
    for i in range(18):
        t.right(140)
        t.forward(80)
        
t.right(60)
t.forward(80)
donut()    
t.forward(100)
donut()

turtle.mainloop()