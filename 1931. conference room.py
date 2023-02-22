import sys
input = sys.stdin.readline

n = int(input())
end_asc = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
end_asc.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간이 같으면 시작하는 시간 오름차 순으로.
end = answer = 0
for s, e in end_asc:
    if s >= end:
        answer += 1
        end = e
print(answer)

# print(board, start_asc, end_asc)
