# 설탕 DP
import sys
input = sys.stdin.readline
dp = [0]*5001
sugar = int(input())
cnt = 0

dp[3] = 1
dp[5] = 1
for i in range(6, sugar+1):
    if dp[i-3]:
        dp[i] = dp[i-3]+1
    if dp[i-5]:
        dp[i] = min(dp[i-5]+1, dp[i]) if dp[i] else dp[i-5]+1
print(dp[sugar]if dp[sugar] != 0 else -1)
