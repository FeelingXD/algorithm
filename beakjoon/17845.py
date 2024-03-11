# 수강 과목
import sys

input = sys.stdin.readline


def solution():
    max_time, case = map(int, input().split())
    dp = [[0] * (max_time + 1) for _ in range(case + 1)]
    time_list = [0]
    score_list = [0]

    for _ in range(case):
        s, t = map(int, input().split())
        time_list.append(t)
        score_list.append(s)

    for c in range(1, case + 1):  # case c
        for t in range(1, max_time + 1):  # time t
            # dp[case][time]=score
            if t < time_list[c]:
                dp[c][t] = dp[c - 1][t]
                continue
            else:
                dp[c][t] = max(
                    dp[c - 1][t], dp[c - 1][t - time_list[c]] + score_list[c]
                )
    print(max(dp[-1]))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
