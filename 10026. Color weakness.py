import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board += list(input().rstrip())

visited = [0] * (n*n)
