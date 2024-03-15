# 가장 긴 증가하는 부분 수열 4
import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    numbers = list(map(int, (input().split())))
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    x = max(dp)
    print(x)

    res = []
    for i in range(N - 1, -1, -1):
        if dp[i] == x:
            res.append(numbers[i])
            x -= 1
    print(*reversed(res))

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
