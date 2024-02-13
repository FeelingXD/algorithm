# BABBA
import sys

input = sys.stdin.readline
A = 0
B = 1


def solution():
    K = int(input())
    dp = [[0] * 2 for _ in range(K + 1)]
    dp[0] = [1, 0]
    for i in range(1, K + 1):
        dp[i][A] = dp[i - 1][B]  # A->B
        dp[i][B] = dp[i - 1][B] + dp[i - 1][A]  # B->BA
    print(*dp[-1])
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
