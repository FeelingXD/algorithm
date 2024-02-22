# 배열 돌리기 1
import sys

input = sys.stdin.readline


def get_board(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def rotate_board(board, round):
    global M, N
    copy_board = [line[:] for line in board]
    square = min(M, N)
    # 보정
    M -= 1
    N -= 1
    for r in range(round):  # 라운드 만큼회전
        if r:  # 회전수가 0이아니면 copy_board 복사하기
            board = [line[:] for line in copy_board]
        for i in range(square // 2):
            for x in range(M - i, i, -1):
                copy_board[i][x - 1] = board[i][x]
            for y in range(i, N - i):
                copy_board[y + 1][i] = board[y][i]
            for x in range(i, M - i):
                copy_board[N - i][x + 1] = board[N - i][x]
            for y in range(N - i, i, -1):
                copy_board[y - 1][M - i] = board[y][M - i]
    return copy_board


def print_board(board):
    for line in board:
        print(*line)


def solution():
    global N, M
    N, M, R = map(int, input().split())  # 세로,가로,회전
    board = get_board(N)
    board = rotate_board(board, R)
    print_board(board)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
