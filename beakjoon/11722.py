# 가장긴 감소하는 부분수열
import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*n

li = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        if li[j] > li[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
