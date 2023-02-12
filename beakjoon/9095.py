# 1,2,3 더하기
import sys
input = sys.stdin.readline


case = []
for i in range(int(input())):
    case.append(int(input()))
maxNum = max(case)

dp = [0]*(maxNum+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxNum+1):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
for i in case:
    print(dp[i])
