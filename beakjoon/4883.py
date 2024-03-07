# 삼각 그래프
import sys

input = sys.stdin.readline


def solution():
    k = 1
    while case := int(input()):
        dp = [list(map(int, input().split())) for _ in range(case)]
        dp[1][0] += dp[0][1]  # 가운데 정점 시작
        dp[1][1] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][0])
        dp[1][2] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][1])
        for i in range(2, len(dp)):
            dp[i][0] += min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] += min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0])
            dp[i][2] += min(dp[i - 1][1], dp[i - 1][2], dp[i][1])
        print(f"{k}. {dp[-1][1]}")
        k += 1

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
