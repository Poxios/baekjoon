width, height = map(int, (input().split()))
board = [list(map(int, input().split())) for _ in range(height)]
day_count = 0
while True:
    stack = []
    for i in range(height):
        for j in range(width):
            if board[i][j] == 1:
                board[i][j] = 2
                if i+1 < height and board[i+1][j] == 0:
                    stack.append((i+1, j))
                if j+1 < width and board[i][j+1] == 0:
                    stack.append((i, j+1))
                if i-1 >= 0 and board[i-1][j] == 0:
                    stack.append((i-1, j))
                if j-1 >= 0 and board[i][j-1] == 0:
                    stack.append((i, j-1))
    if len(stack) == 0:
        break
    for x, y in stack:
        board[x][y] = 1
    day_count += 1

possible = True
for elem in board:
    try:
        elem.index(0)
        possible = False
    except:
        pass

if possible:
    print(day_count)
else:
    print(-1)
