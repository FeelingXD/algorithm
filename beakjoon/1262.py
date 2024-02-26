# 알파벳 다이아몬드
import sys

input = sys.stdin.readline


def alphabet_carpet(n, y1, x1, y2, x2):

    for i in range(y2 - y1 + 1):
        for j in range(x2 - x1 + 1):
            x = (y1 + i) % (2 * n - 1)
            y = (x1 + j) % (2 * n - 1)
            dis = abs((n - 1) - x) + abs((n - 1) - y)

            if dis >= n:
                print(".", end="")
            else:
                print(chr(dis % 26 + ord("a")), end="")
        print()
    pass


def solution():
    N, R1, C1, R2, C2 = map(int, input().split())
    alphabet_carpet(N, R1, C1, R2, C2)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
