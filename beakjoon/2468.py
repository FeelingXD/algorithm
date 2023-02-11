# 안전 영역
from collections import deque
import sys
input = sys.stdin.readline

l = int(input())
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
graph = []
maxNum = 0


def bfs(graph, visited, x, y, value):

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited[x][y] = False
        for d in directions:
            nx = x+d[0]
            ny = y+d[1]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] > value and visited[nx][ny]:
                    visited[nx][ny] = False
                    q.append([nx, ny])


for i in range(l):
    graph.append(list(map(int, input().split())))
    for j in range(l):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

result = 0

for i in range(maxNum):
    visited = [[True]*l for i in range(l)]
    cnt = 0

    for j in range(l):
        for k in range(l):
            if graph[j][k] > i and visited[j][k]:
                bfs(graph, visited, j, k, i)
                cnt += 1

    if result < cnt:
        result = cnt
print(result)
