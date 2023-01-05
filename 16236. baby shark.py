import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
shark_pos = (0, 0)
shark_size = 2
shark_exp = 0
fish = []
time = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for x in range(n):
    for y, v in enumerate(map(int, input().rstrip().split())):
        board.append(v)
        if v == 9:  # baby shark
            shark_pos = (x, y)
        elif v != 0:
            fish.append((x, y))
fish.reverse()  # 가장 위에 있는 물고기가 제일 마지막에 계산되어야 한다.


def bfs(x, y, tx, ty, size) -> int:
    q = deque([(x, y)])
    visited = [0]*(n*n)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            np = nx*n+ny
            if nx == tx and ny == ty:  # 끝
                return visited[x*n+y]+1
            # 다음자리가 벽이거나 이미 방문했거나 물고기인데 나보다 크거나 작으면 넘긴다.
            if (not 0 <= nx < n) or (not 0 <= ny < n) or visited[np] != 0 or (1 <= (fs := board[np]) <= 6 and (size < fs or size > fs)):
                continue

            # 다음으로 나아간다.
            q.append((nx, ny))
            visited[np] = visited[x*n+y]+1
    return -1


while fish:
    # 먹을 수 있는 물고기 중 가장 가까운 물고기를 타겟팅한다.
    # 가장 가까운 물고기가 많다면 가장 좌표가 작은 물고기를 타겟팅.
    # 이미 좌표가 내림차순이기때문에 그냥 순서대로 하면 가장 첫번째꺼가 된다.
    closest_fish_pos = -1
    closest_fish_distance = sys.maxsize
    for fp in [f for f in fish if board[f[0]*n+f[1]] < shark_size]:
        if (temp := bfs(shark_pos[0], shark_pos[1], fp[0], fp[1], shark_size)) != -1 and temp <= closest_fish_distance:
            closest_fish_pos = fp
            closest_fish_distance = temp
    # 먹을 수 있는 물고기가 있다면
    if closest_fish_pos != -1:
        # print('eat!!', closest_fish_pos)
        # 먹고
        fx, fy = closest_fish_pos
        fish.remove((fx, fy))
        board[fx*n+fy] = 0
        # 경험치 업
        shark_exp += 1
        # 레벨업도 한다
        if shark_exp == shark_size:
            shark_exp = 0
            shark_size += 1

        # 시간 반영하고
        time += closest_fish_distance
        # 현재 위치 갱신한다
        shark_pos = (fx, fy)
    else:  # 먹을 수 있는 물고기가 없다면
        print(time)
        exit(0)
print(time)
