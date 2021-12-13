import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import PercolationProblem


def chart(trial, n):
    p = []
    evaluation = []
    for t in range(trial):
        p.append(random.random())
        evaluation.append(PercolationProblem.evaluation(trial, n, p[-1]))
    plt.scatter(p, evaluation, s=4, edgecolors='blue')
    plt.title("Percolation Problem Result")
    plt.xlabel("Probability of open cells")
    plt.ylabel("Percolation probability")
    plt.show()


def main():
    trial = int(input("Please enter the number of times the test was performed:"))
    n = int(input("Specify the size of the matrix:"))
    chart(trial, n)


if __name__ == "__main__":
    main()
