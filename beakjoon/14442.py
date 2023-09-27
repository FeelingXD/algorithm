# 벽부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(n, m, k, board, visited):  # r,c,v
    q = deque()

    q.append([0, 0, k])  # y,x,k
    visited[0][0][k] = 1
    while q:
        y, x, v = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][v]
        for move in moves:
            dx = move[0]
            dy = move[1]
            nx = dx+x
            ny = dy+y
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 0 and not visited[ny][nx][v]:  # 갈수 있는 곳일 경우
                    visited[ny][nx][v] = visited[y][x][v]+1
                    q.append([ny, nx, v])
                # 벽을 깨는 경우
                elif v >= 1 and not visited[ny][nx][v-1] and board[ny][nx] == 1:
                    visited[ny][nx][v-1] = visited[y][x][v]+1
                    q.append([ny, nx, v-1])
    return -1
    pass


def drawboard(n):
    board = []
    for _ in range(n):
        board.append(list(map(int, input().strip())))
    return board
    pass


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = drawboard(n)
    visited = [[[0]*(k+1) for _ in range(len(board[0]))]
               for a in range(len(board))]
    print(bfs(n, m, k, board, visited))
    pass
