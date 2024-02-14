# 블로그
import sys
from itertools import accumulate
import operator

input = sys.stdin.readline


def solution():
    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))
    prefixed = [0] + list(accumulate(visitors))
    ans = 0
    cnt = 0
    for i in range(X, N + 1):
        if (tmp := prefixed[i] - prefixed[i - X]) >= ans:
            if ans == tmp:
                cnt += 1
                continue
            else:
                ans = tmp
                cnt = 1
    print("SAD" if ans == 0 else f"{ans}\n{cnt}")

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
