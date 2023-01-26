# 무인도 여행 BFS
from collections import deque
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
score = 0


def bfs(maps, visited, x, y):
    global score
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    score = int(maps[x][y])
    while queue:
        x, y = queue.popleft()
        for d in dirs:
            nx = x+d[0]
            ny = y+d[1]
            if nx < 0 or ny < 0 or nx >= len(visited) or ny >= len(visited[0]):
                continue
            if visited[nx][ny] == 0:
                continue
            if visited[nx][ny] == 1:
                visited[nx][ny] = 0
                score += int(maps[nx][ny])
                queue.append((nx, ny))


def solution(maps):
    global score
    answer = []
    visited = [[0]*len(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                visited[i][j] = 1

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if visited[i][j] == 1:
                bfs(maps, visited, i, j)
                answer.append(score)
                score = 0
    answer.sort()
    print(answer)
    return [-1] if answer == [] else answer


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
