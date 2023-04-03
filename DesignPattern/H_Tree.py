import turtle


def line_draw(x0 , y0 , x1 , y1):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x0 , y0)
    turtle.pendown()
    turtle.goto(x1 , y1)
    turtle.penup()


def H_tree(depth , x=0 , y=0 , l=140.0):
    if depth > 0:
        line_draw(x - l , y , x + l , y)
        line_draw(x - l , y + l , x - l , y - l)
        line_draw(x + l , y + l , x + l , y - l)
        H_tree(depth - 1 , x - l , y - l , l / 2.0)
        H_tree(depth - 1 , x - l , y + l , l / 2.0)
        H_tree(depth - 1 , x + l , y + l , l / 2.0)
        H_tree(depth - 1 , x + l , y - l , l / 2.0)


def main():
    num = int(input("Please enter the number:"))
    turtle.tracer(100)
    H_tree(num)
    turtle.exitonclick()


if __name__ == "__main__":
    main()