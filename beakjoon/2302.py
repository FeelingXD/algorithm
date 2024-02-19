# 극장 좌석
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    vips = [int(input()) for _ in range(int(input()))]
    vips.sort()
    dp = [1, 1, 2] + [1] * 41  # max

    for i in range(3, 41):
        dp[i] = dp[i - 1] + dp[i - 2]
    ans = 1
    if len(vips):
        prev = 0
        for vip in vips:
            ans *= dp[vip - 1 - prev]
            prev = vip
        ans *= dp[n - prev]
    else:
        ans = dp[n]
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
