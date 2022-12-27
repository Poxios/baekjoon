import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coins = list(int(input()) for _ in range(n))
dp = [1]+[0]*k

for i in coins:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
