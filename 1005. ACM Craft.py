import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    build_time = list(map(int, input().rstrip().split()))
    edge_count = [-1]+[0]*(n)  # 맨 처음껀 제외하고 검사해라
    order = [[] for _ in range(n+1)]
    for _ in range(k):
        front, rear = map(int, input().split())
        edge_count[rear] += 1
        order[front].append(rear)
    final_building = int(input())
    stack = [[idx for idx, x in enumerate(edge_count) if x == 0]]
    win = False
    for s in stack[0]:
        if s == final_building:
            print(build_time[final_building-1])
            win = True
            break
    if win:
        continue
    answer = 0
    while stack:
        cadidate = stack.pop()
        max_building_time = 0
        stack_candidate = []
        for i in cadidate:
            max_building_time = max(max_building_time, build_time[i-1])
            for j in order[i]:
                edge_count[j] -= 1
                if edge_count[j] == 0:
                    # 승리조건이면 이번 턴 끝나고 끝
                    if j == final_building:
                        win = True
                    stack_candidate.append(j)
            if win:
                break
        if stack_candidate:
            stack.append(stack_candidate)
        answer += max_building_time
        if win:
            break
    print(answer+build_time[final_building-1])
