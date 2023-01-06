# 위상정렬
# 자기 앞에 있는 사람이 제일 적은 놈을 꺼내오면 된다.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
height_dic = [[] for _ in range(n+1)]
indegree_lst = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    height_dic[a].append(b)
    indegree_lst[b] += 1  # 진입간선 개수 +1
# 전체에서 진입간선 0인거 찾음
q = deque([idx for idx in range(1, n+1) if indegree_lst[idx] == 0])
while q:
    item = q.popleft()
    for v in height_dic[item]:
        indegree_lst[v] -= 1  # 후방 친구의 진입간선 -1
        if indegree_lst[v] == 0:  # 후방 친구가 혼자면 다음타겟
            q.append(v)
    print(item, end=' ')
