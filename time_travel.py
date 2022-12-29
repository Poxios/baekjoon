import math
import time
import sys

INPUT = 'IEFCJ\
FHFKC\
FFALF\
HFGCF\
HMCHH'


def here():
    board = []
    for e in INPUT.split('\n'):
        board += list(e)


def here2():
    board = []
    for e in INPUT.split('\n'):
        board.append(list(e))


start = time.time()

for i in range(1000000):
    here()

end = time.time()

print(f"{end - start:.5f} sec")
