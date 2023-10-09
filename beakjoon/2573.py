# 빙산
import sys
from collections import deque
input = sys.stdin.readline
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def bfs(y, x):

    queue = deque([[y, x]])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for move in moves:
            dy, dx = move
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                else:
                    cnt[x][y] += 1
    return 1


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
year = 0

while True:
    answer = []
    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(answer) == 0 or len(answer) >= 2:
        break

    year += 1

print(year) if len(answer) >= 2 else print(0)
