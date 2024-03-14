# 벼락치기
import sys

input = sys.stdin.readline


def solution():
    N, T = map(int, input().split())
    scores = [0]
    times = [0]
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    for _ in range(N):
        K, S = map(int, input().split())  # 공부 시간, 배점
        times.append(K)
        scores.append(S)

    for c in range(1, N + 1):
        for t in range(1, T + 1):
            if t < times[c]:
                dp[c][t] = dp[c - 1][t]
                continue
            dp[c][t] = max(dp[c - 1][t - times[c]] + scores[c], dp[c - 1][t])
    print(max(dp[-1]))


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
