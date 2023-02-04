# 1로 만들기
import sys
input = sys.stdin.readline

num = int(input())
dp = [0 for i in range(num+1)]

for i in range(2, num+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[num])
