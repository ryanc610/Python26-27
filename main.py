from myFunctions import *

bob.speed(0)
screen=turtle.Screen()
bob.width(5)
bob.pencolor("light gray")
screen.tracer(0)

for i in range(11):
    jump(-505,i*-86.6+404)
    for num in range(20):
        diamond(50)
        bob.penup()
        bob.forward(50)
        bob.pendown()
    
for i in range(11):
    jump(-530,i*-86.6+447.3)
    for num in range(20):
        diamond(50)
        bob.penup()
        bob.forward(50)
        bob.pendown()
