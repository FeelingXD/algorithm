# 개미전사

# 입력 첫째줄에 창고갯수
# 둘쨋 줄에 저장된 식량 개수 k 가주어질때 개미전사가 얻을수있는 최대값은?
import sys

n = int(sys.stdin.readline().strip())
k = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+k[i])
print(dp[n-1])
