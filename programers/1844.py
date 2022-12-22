# 게임 맵 최단거리

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    return bfs(0, 0, maps)


def bfs(x, y, map: list):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= len(map) or ny >= len(map[0]):
                continue

            if map[nx][ny] == 0:
                continue

            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y]+1
                queue.append((nx, ny))
    return map[len(map)-1][len(map[0])-1] if map[len(map)-1][len(map[0])-1] != 1 else -1
