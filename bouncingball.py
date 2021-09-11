import turtle

turtle.screensize(400,400)
turtle.setworldcoordinates(-200,-200,200,200)
turtle.color('red','black')
turtle.penup()

RADIUS, DT = 2, 15
rx, ry = -30, 50
vx, vy = 5,3

while True:
    if (abs(rx+vx) + RADIUS) > 200:
        vx = -vx
    if (abs(ry+vy) + RADIUS) > 200:
        vy = -vy
    rx += vx
    ry += vy
    turtle.clear()
    turtle.setposition(rx,ry)
    turtle.begin_fill()
    turtle.shape('circle')
    turtle.shapesize(RADIUS)
    turtle.end_fill()
