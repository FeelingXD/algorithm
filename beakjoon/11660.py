import time
import sys
input = sys.stdin.readline

M, cases = map(int, input().split())
dp = [[0]*(M+1) for _ in range(M+1)]
maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

for i in range(1, M+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+maps[i-1][j-1]
for _ in range(cases):
    x1, y1, x2, y2 = map(int, (input().split()))
    print(dp[x2][y2]-(dp[x1-1][y2]+dp[x2][y1-1])+dp[x1-1][y1-1])
