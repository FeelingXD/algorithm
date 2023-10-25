# 연구소
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
PATH = 0
WALL = 1
VIRUS = 2
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0


def solution():
    board = draw_board()
    make_walls(board, 0)
    print(result)
    pass


def get_safe_area(board):
    answer = 0
    for line in board:
        answer += line.count(PATH)
    return answer


def bfs(board):
    global result
    q = deque()
    tmp_board = deepcopy(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == VIRUS:
                q.append((y, x))

    while q:
        cy, cx = q.popleft()
        for move in moves:
            dy, dx = move
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and tmp_board[ny][nx] == PATH:
                tmp_board[ny][nx] = VIRUS
                q.append((ny, nx))
    result = max(get_safe_area(tmp_board), result)


def make_walls(board, d):
    if d == 3:
        # 벽을 3개 놓은 경우
        bfs(board)
        return
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == PATH:
                board[y][x] = WALL
                make_walls(board, d+1)
                board[y][x] = PATH


def draw_board():
    r, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    return board


if __name__ == "__main__":
    solution()
    pass
