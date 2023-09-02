# 1,2,3 더하기 4
import sys
input = sys.stdin.readline

cases = int(input())
dp = [[0 for _ in range(4)] for _ in range(10001)]


def dp_set():  # 항상 오름차순 정렬할 것
    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1  # 1+1+1
    dp[3][2] = 1  # 1+2
    dp[3][3] = 1  # 3

    for i in range(4, 10001):
        dp[i][1] = dp[i-1][1]  # 마지막이 1로 끝나는경우
        dp[i][2] = dp[i-2][1]+dp[i-2][2]
        dp[i][3] = dp[i-3][1]+dp[i-3][2]+dp[i-3][3]


if __name__ == "__main__":
    dp_set()
    for _ in range(cases):
        t = int(input())
        print(sum(dp[t]))
