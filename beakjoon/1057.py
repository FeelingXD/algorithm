# 토너먼트
import sys

input = sys.stdin.readline


def solution():
    N, K, I = map(int, input().split())
    round = 1
    while N > 0:
        for i in range(1, N + 1, 2):
            if set([i, i + 1]) == set([K, I]):
                print(round)
                exit()
        K = K // 2 if not K % 2 else K // 2 + 1
        I = I // 2 if not I % 2 else I // 2 + 1
        round += 1
        N //= 2
    print(-1)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
