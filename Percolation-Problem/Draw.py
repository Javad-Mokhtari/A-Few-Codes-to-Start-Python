import turtle


def white_square(d):
    turtle.pendown()
    turtle.hideturtle()
    turtle.color('gray')
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)


def blue_square(d):
    turtle.pendown()
    turtle.hideturtle()
    turtle.color('gray', 'blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    turtle.end_fill()


def black_square(d):
    turtle.pendown()
    turtle.hideturtle()
    turtle.color('gray', 'black')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    turtle.end_fill()
