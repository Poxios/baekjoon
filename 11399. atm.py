import sys
import heapq
input = sys.stdin.readline
n = input()
heapq.heapify(h := ([*map(int, input().rstrip().split())]))
s = 0
answer = 0
while True:
    try:
        s += heapq.heappop(h)
        answer += s
    except:
        print(answer)
        exit(0)
