# 상범 빌딩
import sys
from collections import deque
input = sys.stdin.readline
WALL = '#'
ROAD = '.'
moves = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]


def search_points(board, l, r, c):
    start, end = 0, 0
    for layer in range(l):
        for row in range(r):
            for colum in range(c):
                if board[layer][row][colum] == 'S':
                    start = (layer, row, colum)
                elif board[layer][row][colum] == 'E':
                    end = (layer, row, colum)

                if start and end:
                    return [start, end]


def bfs(board, l, r, c):
    start, end = search_points(board, l, r, c)
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    answer = -1
    sl, sr, sc = start
    visited[sl][sr][sc] = True
    q = deque([[start, 0]])
    while q:
        position, d = q.popleft()
        cl, cr, cc = position
        if position == end:
            answer = d
        else:
            for move in moves:
                ml, mr, mc = move
                nl, nr, nc = cl+ml, cr+mr, cc+mc

                if 0 <= nl < l and 0 <= nr < r and 0 <= nc < c and board[nl][nr][nc] != WALL and not visited[nl][nr][nc]:
                    visited[nl][nr][nc] = True
                    q.append([(nl, nr, nc), d+1])

    return answer


if __name__ == "__main__":
    while v := tuple(map(int, input().split())):
        l, r, c = v
        if l == r == c == 0:
            break
        board = []
        for _ in range(l):
            layerboard = []
            for _ in range(r):
                layerboard.append(input().strip())
            input()
            board.append(layerboard)
        answer = bfs(board, l, r, c)
        print(
            f'Escaped in {answer} minute(s).' if answer != -1 else "Trapped!")
