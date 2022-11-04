#CTI-110
#P4LAB1c - Snowflake
#Thomas Size
#November 4, 2022

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

#display options
t.pensize(3)
t.pencolor('blue')
t.shape('turtle')

#flake will have 12 'fingers' made up of rhombi

for i in (1,2,3,4,5,6,7,8,9,10,11,12):
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(150)
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(50)
