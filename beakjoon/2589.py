# 보물섬
import sys
from collections import deque

input = sys.stdin.readline
LAND = "L"
SEA = "W"
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def draw_board(rows):
    return [input().strip() for _ in range(rows)]


def validate_oob(y, x) -> bool:
    """
    보드범위를 초과하는지 검사
    """
    return 0 <= y < rows and 0 <= x < cols


def bfs(y, x):
    global board
    visited = [[0] * cols for _ in range(rows)]

    q = deque()
    visited[y][x] = 1
    peek = 1
    q.append((y, x, peek))  # y,x,이동거리 시작이 1 이므로 추후 값을 빼주어야함
    while q:
        cy, cx, v = q.popleft()
        if v > peek:
            peek = v
        for dy, dx in moves:
            ny, nx = cy + dy, cx + dx
            if validate_oob(ny, nx) and not visited[ny][nx] and board[ny][nx] == LAND:
                visited[ny][nx] = v + 1
                q.append((ny, nx, v + 1))
    return peek - 1
    pass


def solution():
    global ans, cols, rows, board
    ans = 0
    rows, cols = map(int, input().split())

    board = draw_board(rows)

    for y in range(rows):
        for x in range(cols):
            if board[y][x] == LAND:
                ans = max(bfs(y, x), ans)
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
