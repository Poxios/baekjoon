import sys
from itertools import combinations
input = sys.stdin.readline
height, width = map(int, input().rstrip().split())
board = []
empty_list = []  # 0
virus_list = []  # 2
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

max_safe_cnt = 0
for i in range(height):
    for idx, v in enumerate(map(int, input().rstrip().split())):
        board.append(v)
        if v == 0:
            empty_list.append(i*width+idx)
        elif v == 2:
            virus_list.append(i*width+idx)

for com in combinations(empty_list, 3):
    visited = [False]*(height*width)
    # 새로 생성된 벽의 개수만큼 없앰.
    safezone = len(empty_list) - 3 + len(virus_list)
    for virus_pos in virus_list:
        stack = [virus_pos]
        while stack:
            c = stack.pop()
            x, y = c//width, c % width
            safezone -= 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                # 영역 안에 있고 빈 공간이고 방문하지 않았고 혹시나 새로 생성된 벽이 아닌 경우
                if (0 <= nx < height) and (0 <= ny < width) and board[(p := (nx*width+ny))] == 0 and (not visited[p]) and (p not in com):
                    stack.append(p)
                    visited[p] = True
    max_safe_cnt = max(max_safe_cnt, safezone)

print(max_safe_cnt)
