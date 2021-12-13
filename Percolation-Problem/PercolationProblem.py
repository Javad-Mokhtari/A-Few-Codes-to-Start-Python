import numpy as np
import random


# The open_cells function returns a matrix that tells us which cell is open with P probability or closed
def open_cells(n, p):
    array01 = np.array([0, 1])
    open_matrix = np.empty([n, n])
    for i in range(n):
        for j in range(n):
            open_matrix[i][j] = random.choices(array01, weights=(1 - p, p))[0]
    return open_matrix


# The full_cells function returns a matrix that tells us which cell is full or empty
def full_cells(n, open_matrix):
    full_matrix = np.zeros([n, n])
    i = 0
    for j in range(n):
        full_matrix = set_full(i, j, full_matrix, open_matrix)
    return full_matrix


# The set_full function starts from first row and recursively fills in the empty cells with according to the obstacles.
def set_full(i, j, full_matrix, open_matrix):
    if i < 0 or i >= len(full_matrix) or j < 0 or j >= len(full_matrix):
        return full_matrix
    if not open_matrix[i][j]:
        return full_matrix
    if full_matrix[i][j]:
        return full_matrix
    full_matrix[i][j] = 1
    full_matrix = set_full(i - 1, j, full_matrix, open_matrix)
    full_matrix = set_full(i + 1, j, full_matrix, open_matrix)
    full_matrix = set_full(i, j - 1, full_matrix, open_matrix)
    full_matrix = set_full(i, j + 1, full_matrix, open_matrix)
    return full_matrix


# The percolation function indicates with a Boolean value whether system has percolation or not
def percolation(n, full_matrix):
    for j in range(n):
        if full_matrix[n - 1][j]:
            return True
    return False


# The evaluation function gives us an estimation of system percolation
def evaluation(trial, n, p):
    count_true = 0
    counter = 0
    for t in range(trial):
        open_matrix = open_cells(n, p)
        full_matrix = full_cells(n, open_matrix)
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
