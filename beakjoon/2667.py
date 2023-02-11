# 단지번호붙이기
from collections import deque
'''
test
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys
input = sys.stdin.readline

lines = int(input())
maps = []
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
apts = []


def bfs(maps, visited, x, y):
    cnt = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        maps[x][y] = 2
        cnt += 1
        for d in direction:
            nx = x+d[0]
            ny = y+d[1]
            if (0 <= nx < lines) and (0 <= ny < lines) and maps[nx][ny] == 1:
                q.append([nx, ny])
                maps[nx][ny] = 2

    apts.append(cnt)


for _ in range(lines):
    maps.append(list(map(int, list(input().strip()))))
visited = [[True] * lines for _ in range(lines)]

for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 1:
            bfs(maps, visited, i, j)
apts.sort()
print(len(apts))
for i in apts:
    print(i)
