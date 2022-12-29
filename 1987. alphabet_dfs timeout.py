import sys
input = sys.stdin.readline
height, width = map(int, input().split())
board = []
for i in range(height):
    board += list(input().rstrip())
max_depth = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y, depth, visited: list, used_char: list):
    global max_depth
    visited[(vp := x*width+y)] = True
    used_char += board[vp]
    max_depth = max(depth, max_depth)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < height) and (0 <= ny < width) and (not visited[(p := (nx*width+ny))]) and (board[p] not in used_char):
            dfs(nx, ny, depth+1, visited[:], used_char[:])


dfs(0, 0, 1, [False]*(height * width), [])
print(max_depth)
