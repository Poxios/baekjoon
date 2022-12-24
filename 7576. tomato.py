from sys import stdin
from collections import deque

width, height = map(int, (stdin.readline().split()))
size = width*height
board = []
for _ in range(height):
    board += list(map(int, stdin.readline().split()))
day_count = -1
indices = deque(i for i, x in enumerate(board) if x == 1)
phase_count = len(indices)
while indices:
    i = indices.pop()
    if i-width >= 0 and board[i-width] == 0:
        indices.appendleft(i-width)
        board[i-width] = 1
    # right
    if ((i+1) % width != 0) and board[i+1] == 0:
        indices.appendleft(i+1)
        board[i+1] = 1
    # down
    if i+width < size and board[i+width] == 0:
        indices.appendleft(i+width)
        board[i+width] = 1
    # left
    if (i % width != 0) and board[i-1] == 0:
        indices.appendleft(i-1)
        board[i-1] = 1

    phase_count -= 1
    if phase_count == 0:
        day_count += 1
        phase_count = len(indices)

if board.count(0) == 0:
    print(day_count)
else:
    print(-1)
