# 섬의 개수
import sys
from collections import deque

input = sys.stdin.readline

moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

SEA = 0
LAND = 1
CHECKED = 2


def draw_board(row) -> list:
    return [list(map(int, input().split())) for _ in range(row)]


def search_island() -> int:
    cnt = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == LAND:
                bfs(y, x)
                cnt += 1
    return cnt


def check_oob(y, x):
    return 0 <= y < r and 0 <= x < c


def bfs(y, x):  # y,x 부터 이동가능한 섬을 탐색
    q = deque()
    q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for dy, dx in moves:
            ny, nx = dy + cy, dx + cx
            if not check_oob(ny, nx):  # 범위 초과시 넘기기
                continue
            if board[ny][nx] == LAND:
                board[ny][nx] = CHECKED
                q.append((ny, nx))

    pass


def solution():
    global board
    global r, c
    while (row_coloum := tuple(map(int, input().split()))) != (0, 0):
        c, r = row_coloum
        board = draw_board(r)
        print(search_island())

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
