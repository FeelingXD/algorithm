# Plane
import sys

input = sys.stdin.readline


def solution():
    n1, k1, n2, k2 = map(int, input().split())
    print(n1 * k1 + n2 * k2)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
