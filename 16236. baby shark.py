import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
shark_pos = (0, 0)
shark_size = 2
fish = []
time = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for x in range(n):
    for y, v in enumerate(map(int, input().rstrip().split())):
        board.append(y)
        if v == 9:  # baby shark
            shark_pos = (x, y)
        elif v != 0:  # fish / {index: size}
            fish.append((x, y))


# (상어와 물고기의 거리, 도착했을 때 몸집)
def bfs(x, y, size, tx, ty) -> tuple:
    q = deque([(x, y, size, 0)])
    visited = [0]*(n*n)
    while q:
        x, y, size, exp = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 벽이거나 이미 방문했으면 넘긴다.
            if (not 0 <= nx < n) or (not 0 <= ny < n) or visited[(np := nx*n+ny)] != 0:
                continue
            if nx == tx and ny == ty:
                # 끝!
                # 해당 물고기 먹고 거리, 사이즈 리턴
                pass
            # 물고기면 확인한다.
            if 1 <= board[np] <= 6:
                # 지나갈 수 없다.
                if size < board[np]:
                    continue

                # 크기가 같으면 지나갈 수 있는데 먹을 수는 없다
                if size == board[np]:
                    q.append((nx, ny, size, exp))
                # 먹으면서 지나갈 수 있다.
                else:
                    fish.remove((nx, ny))  # FIXME
                    exp += 1
                    if exp == size:
                        size += 1
                        exp = 0
                    q.append((nx, ny, size, exp))
                # 거리 입력
                visited[np] = visited[x*n+y]+1
            # 그냥 공기면 그냥 간다.
            else:
                q.append((nx, ny, size, exp))
                visited[np] = visited[x*n+y]+1
    return -1


while fish:
    # 이동할 물고기를 타겟팅한다.
    min_distance_fish = sys.maxsize
    for fp in fish:
        min_distance_fish = min(min_distance_fish, bfs(
            shark_pos[0], shark_pos[1], 2, fp[0], fp[1]))
    print(min_distance_fish)
