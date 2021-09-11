def moves(n , f , t , h):
    if n == 0:
        return
    moves(n - 1 , f , h , t)
    print(str(f) + '-->' + str(t))
    moves(n - 1 , h , t , f)


def main():
    num = int(input("Please enter n:"))
    moves(num , 1 , 3 , 2)


if __name__ == "__main__":
    main()
