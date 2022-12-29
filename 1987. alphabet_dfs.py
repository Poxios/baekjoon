import sys
input = sys.stdin.readline
height, width = map(int, input().split())
board = []
for i in range(height):
    board += map(lambda x: ord(x)-65, list(input().rstrip()))
max_depth = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [False]*26
visited[board[0]] = True


def dfs(x, y, depth):
    global max_depth, visited
    max_depth = max(depth, max_depth)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < height) and (0 <= ny < width) and not visited[(p := board[nx*width+ny])]:
            visited[p] = True
            dfs(nx, ny, depth+1)
            visited[p] = False


dfs(0, 0, 1)
print(max_depth)
