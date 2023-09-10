# 적록 색약

import sys
from collections import deque
input = sys.stdin.readline
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def create_board(size):
    board = []
    for _ in range(size):
        board.append(input().strip())
    return board


def bfs(board, visited, x, y):
    color = board[y][x]
    visited[y][x] = True
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        for move in moves:
            dx, dy = move
            nx, ny = x+dx, y+dy
            if 0 <= nx < board_size and 0 <= ny < board_size and not visited[ny][nx] and board[ny][nx] == color:
                visited[ny][nx] = True
                q.append([nx, ny])


def bfs_RG(board, visited, x, y):
    color = board[y][x]
    visited[y][x] = True
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        for move in moves:
            dx, dy = move
            nx, ny = x+dx, y+dy
            if color in ('G', 'R'):  # 적 녹일경우
                if 0 <= nx < board_size and 0 <= ny < board_size and not visited[ny][nx] and board[ny][nx] in ('G', 'R'):
                    visited[ny][nx] = True
                    q.append([nx, ny])
            else:
                if 0 <= nx < board_size and 0 <= ny < board_size and not visited[ny][nx] and board[ny][nx] == 'B':
                    visited[ny][nx] = True
                    q.append([nx, ny])


if __name__ == "__main__":
    board_size = int(input())
    board = create_board(board_size)
    cnt = 0
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    for y in range(board_size):
        for x in range(board_size):
            if not visited[y][x]:
                cnt += 1
                bfs_RG(board, visited, x, y)
    rg = cnt
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    cnt = 0
    for y in range(board_size):
        for x in range(board_size):
            if not visited[y][x]:
                cnt += 1
                bfs(board, visited, x, y)
    print(f'{cnt} {rg}')
