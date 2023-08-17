# 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# M,N,S
M, N, K = map(int, input().split())

visited = [[False for i in range(N)] for _ in range(M)]
for _ in range(K):  # 사각형 이 놓인곳 visited 처리하기
    v = list(map(int, input().split()))
    s_r, s_c = v[0], v[1]
    e_r, e_c = v[2], v[3]

    for y in range(s_c, e_c):
        for x in range(s_r, e_r):
            visited[y][x] = True


def bfs(visited: list, x: int, y: int, s_area: list):  # size를 재는 bfs
    q = deque()
    visited[y][x] = True
    size = 1
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < len(visited[0]) and 0 <= ny < len(visited) and not visited[ny][nx]:
                size += 1
                q.append([nx, ny])
                visited[ny][nx] = True
    s_area.append(size)


area_list = []
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            bfs(visited, x, y, area_list)

print(len(area_list))
print(*sorted(area_list))
