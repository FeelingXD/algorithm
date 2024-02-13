# RGB거리 2
import sys

input = sys.stdin.readline
R = 0
G = 1
B = 2
I = 10e8


def get_cost(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def solution():
    cost = get_cost(rows := int(input()))
    ans = I

    for j in range(3):
        dp = [[I, I, I] for _ in range(len(cost))]
        dp[0][j] = cost[0][j]
        for i in range(1, len(cost)):
            dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + cost[i][R]
            dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + cost[i][G]
            dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + cost[i][B]
        for k in range(3):
            if j != k:
                ans = min(ans, dp[-1][k])
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
