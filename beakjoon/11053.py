# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
case = int(input())
dp = [0]*(case)

li = list(map(int, input().split()))
for i in range(case):
    dp[i] = 1
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
