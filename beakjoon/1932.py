# 정수 삼각형
import sys
from copy import deepcopy
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [[] for _ in range(n)]
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    dp = deepcopy(board)
    for i in range(1, n):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j]+board[i][j]
            elif j == len(dp[i])-1:
                dp[i][j] = dp[i-1][j-1]+board[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+board[i][j]
    print(max(dp[-1]))
