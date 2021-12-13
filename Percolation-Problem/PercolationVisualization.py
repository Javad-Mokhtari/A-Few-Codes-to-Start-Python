import turtle
import PercolationProblem
import Draw


def visualize(n, open_matrix, full_matrix):
    turtle.tracer(100)
    turtle.setworldcoordinates(-320, -320, 320, 320)
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(-300, 300)
    d = float(600 / n)
    for i in range(n):
        for j in range(n):
            if open_matrix[i][j] and not full_matrix[i][j]:
                Draw.white_square(d)
                turtle.penup()
                turtle.forward(d)
            elif not open_matrix[i][j]:
                Draw.black_square(d)
                turtle.penup()
                turtle.forward(d)
            elif open_matrix[i][j] and full_matrix[i][j]:
                Draw.blue_square(d)
                turtle.penup()
                turtle.forward(d)
        turtle.setx(-300)
        turtle.sety(turtle.ycor()-d)


def main():
    n = int(input("Please enter the size of the matrix:"))
    p = float(input("Also enter the probability of opening cells:"))
    open_matrix = PercolationProblem.open_cells(n, p)
    full_matrix = PercolationProblem.full_cells(n, open_matrix)
    visualize(n, open_matrix, full_matrix)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
