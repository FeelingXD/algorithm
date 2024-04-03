# 색종이
import sys

input = sys.stdin.readline


def solution():
    board = [[0] * 101 for _ in range(101)]
    ans = 0

    for _ in range(case := int(input())):

        cy, cx = map(int, input().split())
        for y in range(cy, cy + 10):
            for x in range(cx, cx + 10):
                board[y][x] = 1

    for line in board:
        ans += sum(line)

    print(ans)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
