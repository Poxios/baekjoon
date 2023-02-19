import sys
input = sys.stdin.readline

n = int(input())

matrix = [input().rstrip() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
answer = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            stack = [(i, j)]
            size = 1
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == '1' and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        size += 1
            answer.append(size)
print(len(answer))
answer.sort()
print('\n'.join(map(str, answer)))
