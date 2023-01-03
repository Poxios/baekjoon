from collections import deque
import sys
input = sys.stdin.readline

height, width = map(int, input().split())
graph = []
for _ in range(height):
    graph += list(map(int, list(input().rstrip())))
visited = [[0] * 2 for _ in range(width*height)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


q = deque([(0, 0, 1)])  # init
visited[0][1] = 1
while q:
    x, y, break_cnt_left = q.popleft()
    if (p := x*width+y) == height*width-1:
        print(visited[p][break_cnt_left])
        exit(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (not 0 <= nx < height) or (not 0 <= ny < width):
            continue
        # 벽 안부수고 (현재 남은 카운트에 상관없이 모두 동작) 다음이 공기고 방문 안했으면
        if graph[(np := nx*width+ny)] == 0 and visited[np][break_cnt_left] == 0:
            q.append((nx, ny, break_cnt_left))
            visited[np][break_cnt_left] = visited[p][break_cnt_left] + 1
        # 다음이 벽이고 벽 부술 수 있는 카운트 남았으면 부수고 이동
        if graph[np] == 1 and break_cnt_left == 1:
            q.append((nx, ny, 0))
            visited[np][0] = visited[p][1] + 1
print(-1)
