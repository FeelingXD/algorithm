# 1로 만들기 2
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]

for x in range(2, n+1):

    # f(x-1)
    dp[x][0] = dp[x-1][0]+1
    dp[x][1] = dp[x-1][1]+[x]

    if not x % 2:
        if dp[x][0] > dp[x//2][0]+1:
            dp[x][0] = dp[x//2][0]+1
            dp[x][1] = dp[x//2][1]+[x]

    if not x % 3:
        if dp[x][0] > dp[x//3][0]+1:
            dp[x][0] = dp[x//3][0]+1
            dp[x][1] = dp[x//3][1]+[x]
print(dp[n][0])
print(*dp[n][1][::-1])
