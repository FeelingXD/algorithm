# 오르막 수
import sys

input = sys.stdin.readline
MOD = 10_007


def solution():
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[1] = [1] * 10
    for i in range(2, len(dp)):
        for j in range(len(dp[0])):
            match j:
                case 0:
                    dp[i][0] += dp[i - 1][0] % MOD
                case n:
                    dp[i][j] += (sum(dp[i - 1][: j + 1])) % MOD

    print(sum(dp[-1]) % MOD)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
