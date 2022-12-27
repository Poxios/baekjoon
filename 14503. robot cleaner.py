import sys
input = sys.stdin.readline
height, width = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
clean_count = 0
while True:
    if board[r][c] == 0:
        clean_count += 1
        board[r][c] = -1
    fail_count = 0

    while True:
        if d == 0:  # up
            next_pos = (r, c-1)  # check left
        elif d == 1:  # right
            next_pos = (r-1, c)  # check up
        elif d == 2:  # down
            next_pos = (r, c+1)  # check right
        elif d == 3:  # left
            next_pos = (r+1, c)  # check down
        if board[next_pos[0]][next_pos[1]] != 0:
            fail_count += 1
        else:
            d = (d-1) % 4
            print('[next]moved to', next_pos, d)
            r, c = next_pos
            break

        if fail_count == 4:
            break
        d = (d-1) % 4

    if fail_count == 4:
        if d == 0:  # up
            rear_pos = (r+1, c)
        elif d == 1:  # right
            rear_pos = (r, c-1)
        elif d == 2:  # down
            rear_pos = (r-1, c)
        elif d == 3:  # left
            rear_pos = (r, c+1)

        if board[rear_pos[0]][rear_pos[1]] == 1:
            break
        else:
            print('[rear]moved to', rear_pos, d)
            r, c = rear_pos


print(clean_count)
