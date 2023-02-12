# 그림

from collections import deque
import sys
input = sys.stdin.readline


c, r = map(int, input().split())
paint = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt = 0
maxarea = 0


def bfs(maps, x, y):

    q = deque()
    q.append([x, y])
    maps[x][y] = 2
    area = 1
    while q:
        x, y = q.popleft()
        for d in directions:
            nx = x+d[0]
            ny = y+d[1]
            if (0 <= nx < c) and (0 <= ny < r) and maps[nx][ny] == 1:
                maps[nx][ny] = 2
                area += 1
                q.append([nx, ny])
    return area


for i in range(c):
    paint.append(list(map(int, input().split())))

for i in range(c):
    for j in range(r):
        if paint[i][j] == 1:
            maxarea = max(bfs(paint, i, j), maxarea)
            cnt += 1
print(cnt)
print(maxarea)
