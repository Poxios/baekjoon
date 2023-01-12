import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

height, width = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(height)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dp = [[-1]*width for _ in range(height)]
dp[0][0] = 1


def dfs(x, y):
    temp = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < height and 0 <= ny < width and matrix[nx][ny] > matrix[x][y]:
            if dp[nx][ny] == -1:
                dfs(nx, ny)
            temp += dp[nx][ny]
    dp[x][y] = temp


dfs(height-1, width-1)


print(dp[height-1][width-1])
