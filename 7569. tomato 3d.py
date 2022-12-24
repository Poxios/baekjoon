import sys
from collections import deque
input = sys.stdin.readline
width, height, h = map(int, input().split())
board = []
for _ in range(h):
    board.append([list(map(int, input().split())) for _ in range(height)])

queue = deque()

for z in range(h):
    for y in range(height):
        for x in range(width):
            if board[z][y][x] == 1:
                queue.append((x, y, z))
day_count = 0
queue_size = len(queue)
while len(queue) != 0:
    x, y, z = queue.pop()
    # above
    if z != h-1 and board[z+1][y][x] == 0:
        board[z+1][y][x] = 1
        queue.appendleft((x, y, z+1))
    # below
    if z != 0 and board[z-1][y][x] == 0:
        board[z-1][y][x] = 1
        queue.appendleft((x, y, z-1))
    # up
    if y != 0 and board[z][y-1][x] == 0:
        board[z][y-1][x] = 1
        queue.appendleft((x, y-1, z))
    # down
    if y != height-1 and board[z][y+1][x] == 0:
        board[z][y+1][x] = 1
        queue.appendleft((x, y+1, z))
    # left
    if x != 0 and board[z][y][x-1] == 0:
        board[z][y][x-1] = 1
        queue.appendleft((x-1, y, z))
    # right
    if x != width-1 and board[z][y][x+1] == 0:
        board[z][y][x+1] = 1
        queue.appendleft((x+1, y, z))

    queue_size -= 1
    if queue_size == 0:
        day_count += 1
        queue_size = len(queue)

for floor in board:
    for row in floor:
        for elem in row:
            if elem == 0:
                print(-1)
                exit(0)
print(day_count-1)
