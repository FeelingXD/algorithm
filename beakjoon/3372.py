# 보드점프
import sys
from collections import deque
input = sys.stdin.readline


def drawboard(n):
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    return board
    pass


def solution():
    n = int(input())
    board = drawboard(n)
    return bfs(n, board)
    pass


def bfs(n, board):

    dp = [[0]*n for _ in range(n)]
    dp[0][0] = 1
    for y in range(n):
        for x in range(n):
            if v := board[y][x]:
                if y+v < n:
                    dp[y+v][x] += dp[y][x]
                if x+v < n:
                    dp[y][x+v] += dp[y][x]
    return dp[-1][-1]


if __name__ == "__main__":
    print(solution())
    pass
