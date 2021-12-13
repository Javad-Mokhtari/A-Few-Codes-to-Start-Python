import numpy as np
import random


# The is_open function returns a matrix that tells us which cell is open with P probability or closed
def is_open(n, p):
    array01 = np.array([0, 1])
    open_matrix = np.empty([n, n])
    for i in range(n):
        for j in range(n):
            open_matrix[i][j] = random.choices(array01, weights=(1-p, p))[0]
    return open_matrix


# The is_full function returns a matrix that tells us which cell is full or empty
def is_full(n, open_matrix):
    full_matrix = np.empty([n, n])
    for j in range(n):
        full_matrix[0][j] = open_matrix[0][j]
    for i in range(1, n):
        for j in range(n):
            if full_matrix[i - 1][j] and open_matrix[i][j]:
                full_matrix[i][j] = 1
            else:
                full_matrix[i][j] = 0
    return full_matrix


# The percolation function indicates with a Boolean value whether system has percolation or not
def percolation(n, full_matrix):
    for j in range(n):
        if full_matrix[n-1][j]:
            return True
    return False


# The evaluation function gives us an estimation of system percolation
def evaluation(trial, n, p):
    count_true = 0
    counter = 0
    for t in range(trial):
        open_matrix = is_open(n, p)
        full_matrix = is_full(n, open_matrix)
        if percolation(n, full_matrix):
            count_true += 1
        counter += 1
    return float(count_true / counter)


def main():
    trial = int(input("Please enter the number of times the test was performed:"))
    n = int(input("Specify the size of the matrix:"))
    p = float(input("Also Enter the probability of opening cells:"))
    print('The probability of vertical percolation is:', evaluation(trial, n, p) * 100, '%')


if __name__ == '__main__':
    main()
