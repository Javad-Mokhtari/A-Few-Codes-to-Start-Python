'''
In the random walk problem ٫ we move randomly in one of the four directions up ٫ down ٫ left or right in a n×n network.
This code specifies the percentage of times the stimulus reaches a dead end.
'''
import random

n = int(input("Enter the number of the latice size:"))
trials = int(input("Enter the number of times the tests should be performed:"))
dead_ends = 0
for t in range(trials):
    a = [[False] * n for i in range(n)]
    x , y = n // 2 , n // 2
    while (0 < x < n - 1) and (0 < y < n - 1):
        if a[x][y + 1] and a[x][y - 1] and a[x - 1][y] and a[x + 1][y]:
            dead_ends += 1
            break
        a[x][y] = True

        r = random.randrange(1 , 5)
        if r == 1 and not a[x][y + 1]:
            y += 1
        elif r == 2 and not a[x][y - 1]:
            y -= 1
        elif r == 3 and not a[x - 1][y]:
            x -= 1
        elif r == 4 and not a[x + 1][y]:
            x += 1
print(dead_ends * 100 / trials , '%')
