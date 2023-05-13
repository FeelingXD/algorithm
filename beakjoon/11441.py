# 합구하기
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1]+li[i-1]
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[e]-dp[s-1])
