import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [2]+[0]*(n*n-1)
# apple: 1
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
my_body = deque([0])

while True:
    (x, y) = pos
    time += 1

    # 방향 회전을 해야할 타이밍인지 확인, 방향 수정
    if time in rotate_timing:
        print('rotate!!', time, (x, y))
        if rotate_timing[time] == 'L':  # 좌회전
            direction = (direction-1) % 4
        else:  # 우회전
            direction = (direction+1) % 4

    # 다음 칸이 벽이거나 내 몸이면 끝
    if (not 0 <= (nx := x+dx[direction]) < n) or (not 0 <= (ny := y+dy[direction]) < n):
        print('next is wall')
        break
    if board[(p := nx*n+ny)] == 2:
        print('next is me')
        break
    # 다음 칸이 사과이면 꼬리 보존, 다음 칸이 공기면 꼬리 삭제
    if board[p] == 0:
        board[my_body.popleft()] = 0
    # 머리 전진, 머리 커서 이동
    board[p] = 2
    my_body.append(p)
    pos = (nx, ny)

    # Debug
    for i in range(n):
        for j in range(n):
            print(board[i*n+j], end='')
        print('')
    print('')
print(time+1)
