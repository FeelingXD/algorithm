# 펠린드롬?
import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        dp[i][i] = True
    for i in range(N - 1):
        if numbers[i] == numbers[i + 1]:
            dp[i][i + 1] = True
        else:
            dp[i][i + 1] = False
    for cnt in range(N - 2):
        for i in range(N - 2 - cnt):
            j = i + 2 + cnt
            if numbers[i] == numbers[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
    for _ in range(case := int(input())):
        s, e = map(int, input().split())
        print(1 if dp[s - 1][e - 1] else 0)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
