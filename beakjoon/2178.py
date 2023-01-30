# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline


def bfs(r, c, m, count):
    cnt = 1
    q = deque()
    count[r][c] = 1
    q.append((r, c))
    while (q):
        x, y = q.popleft()
        for d in dirs:
            nx = x+d[0]
            ny = y+d[1]
            if nx < 0 or len(m) <= nx or ny < 0 or len(m[0]) <= ny:
                continue
            if m[nx][ny] == '1' and count[nx][ny] == 0:
                count[nx][ny] = count[x][y]+1
                q.append((nx, ny))


dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
r, c = map(int, input().split())
maps = []
counts = [[0 for _ in range(c)] for _ in range(r)]
for _ in '*'*r:
    maps.append(input().strip())

bfs(0, 0, maps, counts)
print(counts[r-1][c-1])
