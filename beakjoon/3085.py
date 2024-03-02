# 사탕 게임
import sys

input = sys.stdin.readline
moves = [(0, 1), (0, -1), (-1, 0), (0, 1)]


def draw_board(rows):
    return [list(input().strip()) for _ in range(rows)]


def check_line(line):  # 행과 열 검사
    global ans
    cnt = 1
    max_cnt = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
    ans = max(ans, max_cnt)
    pass


def dfs(board, n):
    for y in range(n):
        for x in range(n):
            check_line(board[y])
            check_line([row[x] for row in board])
    if ans == n:  # fast fail
        return

    for y in range(n):
        for x in range(n):
            for dy, dx in moves:
                if not (0 <= (ny := y + dy) < n and 0 <= (nx := x + dx) < n):
                    continue
                board[ny][nx], board[y][x] = board[y][x], board[ny][nx]  # 위치 바꿔주기
                check_line(board[ny])
                check_line(board[ny - dy])
                check_line([row[nx - dx] for row in board])
                check_line([row[nx] for row in board])
                board[ny][nx], board[y][x] = board[y][x], board[ny][nx]  # 위치 바꿔주기
    pass


def solution():
    global ans
    ans = 1
    n = int(input())  # 보드 크기
    board = draw_board(n)
    dfs(board, n)
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
