import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [0]*(n*n)
# apple
for i in range(int(input())):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x*n+y] = 1

# rotate
rotate_timing = {}
for _ in range(int(input())):
    temp = input().split()
    rotate_timing[int(temp[0])] = temp[1]

time = 0
direction = 1  # up right down left
pos = (0, 0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
my_body = deque([])

while True:
    x, y = pos
    # 시간은 흐른다
    time += 1
    # 현재 칸은 내 몸이다.
    board[x*n+y] = 2
    my_body.append(x*n+y)
    # 방향 회전을 해야할 타이밍인지 확인, 방향 수정
    if time in rotate_timing:
        print('rotate!!', time, (x, y))
        if rotate_timing[time] == 'L':  # 좌회전
            direction = (direction-1) % 4
        else:  # 우회전
            direction = (direction+1) % 4

    # 다음 칸이 벽이거나 내 몸이면 끝
    if (not 0 <= (nx := x+dx[direction]) < n) or (not 0 <= (ny := y+dy[direction]) < n) or board[(p := nx*n+ny)] == 2:
        break
    # 다음 칸이 사과이면 꼬리 보존, 다음 칸이 공기면 꼬리 삭제
    if board[p] == 0:
        board[my_body.popleft()] = 0

    # DEBUG
    if board[p] == 1:
        print('got apple!!', nx, ny)
    # 머리 움직임
    pos = (nx, ny)
    # print(len(my_body))
print(time)
