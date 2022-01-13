import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

mick = turtle.Turtle()
mick.shape("circle")
mick.color("yellow")
mick.speed(8)
mick.penup()

side = 125
for _ in range(120):
    mick.forward(side)
    mick.stamp()
    mick.right(80)   
    side = side - 6

wn.exitonclick()