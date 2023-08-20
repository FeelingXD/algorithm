# 토마토
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
visited = [[False for _ in range(N)] for _ in range(M)]
board = []
for _ in range(M):
    board.append(list(map(int, input().split())))


def find_tomato(board, visited):
    li = []
    for y in range(M):
        for x in range(N):
            if board[y][x] == 1:
                visited[y][x] = True
                li.append([x, y, 0])
            elif board[y][x] == -1:
                visited[y][x] = True
    return li


def bfs(board, visited):
    preset_tomato = find_tomato(board, visited)
    q = deque(preset_tomato)
    answer = 0
    while q:
        x, y, depth = q.popleft()
        if depth > answer:
            answer = depth
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                visited[ny][nx] = True
                board[ny][nx] = 1
                q.append([nx, ny, depth+1])

    for y in range(M):
        if 0 in board[y]:
            return -1

    return answer


print(bfs(board, visited))
