from sys import stdin
from math import sqrt
n = int(stdin.readline())

arr = [True]*(n+1)
arr[0] = arr[1] = False
for i in range(2, int(sqrt(n))+1):
    if arr[i]:
        for j in range(i*2, n+1, i):
            arr[j] = False

start = 0
end = 0
answer = 0
arr = [i for i in range(n+1) if arr[i]]
while end != len(arr):
    s = 0
    for i in range(start, end+1):
        s += arr[i]
    if s == n:
        answer += 1
        start += 1
        end += 1
    elif s < n:
        end += 1
    else:
        start += 1

print(answer)
