'''
مساله ولگشت خودگریز که یک عامل در یک شبکه n*n شروع به جرکت تصادفی در یکی از چهار جهت بالا پایین چپ راست میکند و این کد تعیین میکند در چند درصد مواقع
عامل به بن بست میرسد. یعنی اگر در یک جهت حرکت کند به نقطه ای که قبلا ملاقات شده می رسد.
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
