# 이친수
import sys

input = sys.stdin.readline


n = int(input())

dp = [[0, 0] for i in range(n+1)]

dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n+1):
    if dp[i-1][0] >= 1:
        dp[i][0] += dp[i-1][0]
        dp[i][1] += dp[i-1][0]
    if dp[i-1][1] >= 1:
        dp[i][0] += dp[i-1][1]

print(sum(dp[n]))
