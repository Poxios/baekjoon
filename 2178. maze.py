import sys
from collections import deque
input = sys.stdin.readline

height, width = map(int, input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
matrix = []
visited = [[0]*width for _ in range(height)]
for _ in range(height):
    matrix.append(input().rstrip())

queue = deque([(0, 0)])
visited[0][0] = 1

while True:
    x, y = queue.popleft()
    if x == height-1 and y == width-1:
        print(visited[x][y])
        exit(0)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < height and 0 <= ny < width and matrix[nx][ny] == '1' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
