import math
import time
import sys


def here():
    board = [True in range(10**6)]
    cnt = 0
    for v in board:
        if v == True:
            cnt += 1


start = time.time()

for i in range(1000000):
    here()

end = time.time()

print(f"{end - start:.5f} sec")
