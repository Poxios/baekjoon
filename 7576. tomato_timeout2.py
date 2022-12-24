width, height = map(int, (input().split()))
board = []
for _ in range(height):
    board += list(map(int, input().split()))
day_count = 0

while True:
    indices = [i for i, x in enumerate(board) if x == 1]
    if len(indices) == 0:
        break
    day_count += 1
    for i in indices:
        board[i] = 2
        # up
        if i-width >= 0 and board[i-width] == 0:
            board[i-width] = 1
        # right
        if ((i+1) % width != 0) and board[i+1] == 0:
            board[i+1] = 1
        # down
        if i+width < len(board) and board[i+width] == 0:
            board[i+width] = 1
        # left
        if (i % width != 0) and board[i-1] == 0:
            board[i-1] = 1

if board.count(0) == 0:
    print(day_count-1)
else:
    print(-1)
