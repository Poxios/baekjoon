import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [2]+[0]*(n*n-1)
# apple: 1
for i in range(int(input())):
    x, y = map(int, input().split())
    board[(x-1)*n+(y-1)] = 1

# rotate
rotate_timing = {}
for _ in range(int(input())):
    temp = input().split()
    rotate_timing[int(temp[0])] = temp[1]

time = 1
direction = 1  # up right down left
x, y = (0, 0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
my_body = deque([0])

while 0 <= (x := x+dx[direction]) < n and 0 <= (y := y+dy[direction]) < n and board[(p := x*n+y)] != 2:
    if board[p] == 0:
        board[my_body.popleft()] = 0
    board[p] = 2
    my_body.append(p)
    # 방향 회전을 해야할 타이밍인지 확인, 방향 수정
    if time in rotate_timing:
        if rotate_timing[time] == 'L':  # 좌회전
            direction = (direction-1) % 4
        else:  # 우회전
            direction = (direction+1) % 4

    time += 1
print(time)
