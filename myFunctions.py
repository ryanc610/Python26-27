import turtle
import random
bob = turtle.Turtle()

bob.speed(0)
turtle.colormode(255)
def jump(x,y):
   bob.penup()
   bob.goto(x,y)
   bob.pendown()
def diamond(size):
    r = random.randint(230, 250)
    b = random.randint(160, 195)
    g = random.randint(210, 235)
    color = (r,g,b)
    bob.fillcolor(color)
    bob.begin_fill()
    bob.left(60)
    bob.forward(size)
    bob.right(120)
    bob.forward(size)
    bob.right(60)
    bob.forward(size)
    bob.right(120)
    bob.forward(size)
    bob.end_fill()
    bob.setheading(0)
