import io
import os
# import sys
from collections import deque
# input = sys.stdin.readline
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    time = [-1]+list(map(int, input().split()))
    order = [[] for _ in range(n+1)]
    edge_count = [0]*(n+1)
    dp = [0]*(n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        order[a].append(b)
        edge_count[b] += 1

    q = deque()
    for i in range(1, n+1):
        if edge_count[i] == 0:
            dp[i] = time[i]  # 혼자 엄청 길 수도 있음.
            q.append(i)

    while q:
        build_idx = q.popleft()
        for i in order[build_idx]:
            dp[i] = max(dp[i], dp[build_idx]+time[i])  # 자체로 지어지는 시간이 길면 그냥 둠
            edge_count[i] -= 1
            if edge_count[i] == 0:
                q.append(i)

    print(dp[int(input())])
