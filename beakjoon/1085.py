# 직사각형에서 탈출
import sys

input = sys.stdin.readline


def solution():
    x, y, w, h = map(int, input().split())
    print(min([abs(0 - x), abs(0 - y), abs(w - x), abs(h - y)]))

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
