import turtle
import math
import random


def chaos():

    a, b = -100.0, -100.0
    c, d = 100.0, math.sqrt(3.0) * 200.0 - 100
    e, f = 300.0, -100.0
    n = 1000000

    turtle.penup()
    turtle.hideturtle()
    turtle.tracer(1000)
    turtle.speed('fastest')
    turtle.setposition(a, b)
    turtle.dot(5, 'red')
    turtle.setposition(c, d)
    turtle.dot(5, 'blue')
    turtle.setposition(e, f)
    turtle.dot(5, 'green')
    turtle.exitonclick()

    for i in range(n):
        rnd = random.randrange(1, 4)
        pos = turtle.position()
        if rnd == 1:
            x = (turtle.xcor() + a) / 2.0
            y = (turtle.ycor() + b) / 2.0
            turtle.setposition(x, y)
            turtle.dot(1, 'red')
        elif rnd == 2:
            x = (turtle.xcor() + c) / 2.0
            y = (turtle.ycor() + d) / 2.0
            turtle.setposition(x, y)
            turtle.dot(1, 'blue')
        elif rnd == 3:
            x = (turtle.xcor() + e) / 2.0
            y = (turtle.ycor() + f) / 2.0
            turtle.setposition(x, y)
            turtle.dot(1, 'green')

    turtle.done()


if __name__ == '__main__':
    chaos()