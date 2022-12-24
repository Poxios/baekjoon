from sys import stdin, maxsize
from itertools import combinations
input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))
answer = maxsize

for com in combinations(chicken, m):
    total_distance = 0
    for h in house:
        total_distance += min(abs(h[0]-c[0])+abs(h[1]-c[1]) for c in com)
    answer = min(answer, total_distance)

print(answer)
