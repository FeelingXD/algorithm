# 인공지능 시계
import sys

input = sys.stdin.readline


def solution():
    h, m, s = map(int, input().split())
    D = int(input())
    nh, lo = divmod(D, 3600)
    nm, lo = divmod(lo, 60)

    if (s + lo) // 60:
        nm += 1
        s = (s + lo) % 60
    else:
        s = s + lo
    if (nm + m) // 60:
        nh += 1
        m = (m + nm) % 60
    else:
        m = nm + m
    if (h + nh) // 24:
        h = (h + nh) % 24
    else:
        h += nh

    print(h, m, s, sep=" ")
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
