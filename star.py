import turtle
wn = turtle.Screen()

mick = turtle.Turtle()
mick.pensize(1)
mick.color("purple")
mick.speed(9)

side = 200
for _ in range(100):
	mick.forward(side)
	mick.right(144)
	side = side - 2
