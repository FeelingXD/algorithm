# 이친수
import sys

input = sys.stdin.readline


def solution():
    """
    stdout : N자리의 이친수의 갯수
    이친수
    1. 이친수는 0으로 시작하지 않는다.
    2. 이친수에서는 1이 두 번 연속으로 나타나지 않는다.
     - 즉, 11을 부분 문자열로 갖지 않는다.
    """
    N = int(input())
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1] = [0, 1]
    for i in range(2, len(dp)):
        dp[i][1] += dp[i - 1][0]
        dp[i][0] += dp[i - 1][0] + dp[i - 1][1]
    print(sum(dp[-1]))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
