# why is js faster?
# 어쩔땐 통과하고 어쩔땐 막힘.
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
board = [(x//n, x % n) for x in range(n*n)]


def dfs(depth, pos, candidate):
    global n, cnt
    # success case
    if depth == n:
        cnt += 1
        return
    candidate = [e for e in candidate if e[0] != pos[0] and e[1] != pos[1] and
                 abs(e[0]-pos[0]) != abs(e[1]-pos[1])]

    for c in candidate:
        if c[0] != depth:
            break
        dfs(depth+1, c, candidate.copy())


for i in range(n):
    dfs(1, (0, i), board)
print(cnt)
