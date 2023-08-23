# 영재의 징검다리
import sys

input = sys.stdin.readline

mod = 1_000_000_007
N, M = map(int, input().split())  # y,x
board = [list(map(int, input().split())) for _ in range(N)]
# preset board
dp = [[0 for i in range(M)]for _ in range(N)]

dp[N-1] = board[N-1]

for y in range(N-2, -1, -1):
    for x in range(M):
        if board[y][x] == 1:
            dp[y][x] += dp[y+1][x]

            if x-1 >= 0:
                dp[y][x] += dp[y+1][x-1]
            if x+1 < M:
                dp[y][x] += dp[y+1][x+1]

            dp[y][x] %= mod
print(sum(dp[0]) % mod)
