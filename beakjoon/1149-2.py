# RGB 거리
import sys

input = sys.stdin.readline

R, G, B = 0, 1, 2


def solution():
    N = int(input())
    streets = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N + 1)]
    dp[1] = streets[0]
    for i in range(2, N + 1):
        dp[i][R] = min(dp[i - 1][B], dp[i - 1][G]) + streets[i - 1][R]
        dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + streets[i - 1][G]
        dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + streets[i - 1][B]
    pass
    print(min(dp[-1]))


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
