import turtle

turtle.bgcolor("white")
turtle.pensize(5)
def kalp():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red","red")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
kalp()

turtle.left(120)
kalp()
turtle.forward(11.65)
turtle.end_fill()
turtle.hideturtle()


