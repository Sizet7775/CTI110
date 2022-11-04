#CTI-110
#P4LAB1a - Shapes
#Thomas Size
#November 4, 2022

import turtle
win = turtle.Screen()
t = turtle.Turtle()

#display options
t.pensize(4)
t.pencolor('black')
t.shape('turtle')

#square has 4 sides 360/4 = 90
#triangle has 3 sides 360/3 = 120

for i in (1,2,3,4):
    t.forward(100)
    t.left(90)
else:
    for i in (1,2,3):
        t.forward(100)
        t.left(120)
