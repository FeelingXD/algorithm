# 1,2,3 더하기 3
import sys
input = sys.stdin.readline


def dp_set(dp):
    n = len(dp)
    if n in (1, 2, 3, 4):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            return 7
    dp[1], dp[2], dp[3], dp[7] = 1, 2, 4, 7
    for i in range(4, len(dp)):
        dp[i] = (dp[i-3]+dp[i-2]+dp[i-1]) % 1_000_000_009


if __name__ == "__main__":
    case = int(input())
    dp = [-1 for _ in range(1000001)]
    dp_set(dp)
    for _ in range(case):
        T = int(input())
        print(dp[T])
