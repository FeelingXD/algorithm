# 배열 돌리기 1
import sys

input = sys.stdin.readline


def get_board(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def rotate_board(board, round):
    global M, N
    square = min(M, N)
    # 보정
    M -= 1
    N -= 1
    for _ in range(round):  # 라운드 만큼회전
        for i in range(square // 2):
            prev = board[i][i]  # 좌표상단 꼭짓점 초기 값 등록
            for y in range(i, N - i):
                board[y + 1][i], prev = prev, board[y + 1][i]
            for x in range(i, M - i):
                board[N - i][x + 1], prev = prev, board[N - i][x + 1]
            for y in range(N - i, i, -1):
                board[y - 1][M - i], prev = prev, board[y - 1][M - i]
            for x in range(M - i, i, -1):
                board[i][x - 1], prev = prev, board[i][x - 1]
    return board


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
