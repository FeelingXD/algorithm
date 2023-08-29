# 스티커
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = int(input())
    board = [[0 for _ in range(l)] for _ in range(2)]
    dp = [[0 for _ in range(l+1)] for _ in range(3)]

    board[0] = list(map(int, input().split()))
    board[1] = list(map(int, input().split()))

    # dp logic
    dp[1][1] = board[0][0]
    dp[2][1] = board[1][0]
    for x in range(2, len(dp[0])):
        for y in range(1, len(dp)):
            if y == 1:
                dp[y][x] = max(dp[y+1][x-1]+board[y-1][x-1],
                               dp[y+1][x-2]+board[y-1][x-1])
            else:
                dp[y][x] = max(dp[y-1][x-1]+board[y-1][x-1],
                               dp[y-1][x-2]+board[y-1][x-1])
    print(max(dp[-1][-1], dp[-2][-1]))
