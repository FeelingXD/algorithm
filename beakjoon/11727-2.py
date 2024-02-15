# 2xn 타일링 2
import sys

input = sys.stdin.readline
MOD = 10_007


def solution():
    n = int(input())
    dp = [0] * (1000 + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print(dp[n] % MOD)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
