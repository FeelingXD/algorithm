# 이차원 배열과 연산
import sys
from collections import defaultdict

input = sys.stdin.readline


def draw_board(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def validate_oob(board):
    y, x = len(board), len(board[0])
    return 0 <= r < y and 0 <= c < x


def solution():
    global r, c
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    board = draw_board(3)
    t = 0
    for t in range(101):
        if validate_oob(board) and board[r][c] == k:
            print(t)
            exit()

        rmode = True
        if len(board) < len(board[0]):  # C 연산일 경우 전치행렬 변환
            rmode = False
            board = list(map(list, zip(*board)))
        maxcol = 0
        for y in range(len(board)):
            cnts = defaultdict(int)
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    continue
                cnts[board[y][x]] += 1

            items = sorted(cnts.items(), key=lambda x: (x[1], x[0]))
            board[y] = [value for sublist in items for value in sublist]

            maxcol = max(maxcol, len(board[y]))

        maxcol = min(maxcol, 100)
        for y in range(len(board)):
            if len(board[y]) < maxcol:
                board[y] = board[y] + [0] * (maxcol - len(board[y]))
            elif len(board[y]) > maxcol:
                board[y] = board[y][:100]

        if not rmode:  # 열연산을 햇을경우 다시변환
            board = list(map(list, zip(*board)))
    print(-1)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
