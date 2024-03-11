# 포도주 시음
import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())  # 갯수와 ,주량
    wines = [0] + list(map(int, input().split()))
    wines.sort()
    prev = 0
    end = len(wines) - 1
    cnt = 0
    ans = 0
    while cnt < K:
        if cnt % 2:
            prev += 1
            cnt += 1
        else:
            ans += wines[end] - wines[prev]
            end -= 1
            cnt += 1
    print(ans)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
