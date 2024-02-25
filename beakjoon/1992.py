# 쿼드트리
import sys

input = sys.stdin.readline


def get_board(rows):
    return [input().strip() for _ in range(rows)]


def solution():
    l = int(input())
    board = get_board(l)
    answer = ""

    def compression(y, x, l):  # 압축
        nonlocal answer
        start = board[y][x]
        for row in range(y, y + l):
            for col in range(x, x + l):
                if board[row][col] != start:
                    l //= 2
                    answer += "("
                    compression(y, x, l)
                    compression(y, x + l, l)
                    compression(y + l, x, l)
                    compression(y + l, x + l, l)
                    answer += ")"
                    return
                    pass
        answer += start

    compression(0, 0, l)
    print(answer)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
