import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board += list(input().rstrip())
visited = [0]*(n*n)

total_cnt = weak_cnt = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, prefix):
    visited[x*n+y] += 1
    curr_char = board[x*n+y]

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n) and visited[nx*n + ny] == prefix and board[nx*n + ny] == curr_char:
            dfs(nx, ny, prefix)


for i in range(n):
    for j in range(n):
        if visited[i*n+j] == 0:
            total_cnt += 1
            dfs(i, j, 0)

board = ['R' if x == 'G' else x for x in board]

for i in range(n):
    for j in range(n):
        if visited[i*n+j] == 1:
            dfs(i, j, 1)
            weak_cnt += 1

print(total_cnt, weak_cnt)
