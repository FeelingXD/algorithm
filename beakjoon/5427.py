# 불
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
FIRE = '*'
WALL = '#'
SANGEUN = '@'
PATH = '.'
FAIL = "IMPOSSIBLE"


def draw_maps(row):
    maps = []
    for _ in range(row):
        maps.append(input().strip())
    return maps


def find_fires(maps):
    fires = []
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == FIRE:
                fires.append((y, x))
    return fires


def find_str(maps):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == SANGEUN:
                return (y, x)


def solution(c, r, maps):
    print(bfs(maps, r, c))
    pass


def bfs(maps, r, c):
    visited = [[0]*c for _ in range(r)]
    q = deque()

    fires = find_fires(maps)
    for fire in fires:
        y, x = fire
        q.append((y, x))
        visited[y][x] = -1  # 불은 -1 표시

    y, x = find_str(maps)
    q.append((y, x))
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for move in moves:
            dy, dx = move
            ny, nx = y+dy, x+dx
            # 지도를 벗어난경우
            if ((nx < 0 or nx >= c) or (ny < 0 or ny >= r)) and visited[y][x] > 0:
                return visited[y][x]
            elif 0 <= nx < c and 0 <= ny < r and visited[ny][nx] == 0:
                if visited[y][x] < 0:  # 불인경우
                    if maps[ny][nx] != WALL:  # 벽이아닐경우 번지기
                        visited[ny][nx] = -1
                        q.append((ny, nx))
                    pass
                elif visited[y][x] > 0:  # 사람이 이동할경우
                    if not visited[ny][nx] and maps[ny][nx] not in (FIRE, WALL):
                        visited[ny][nx] = visited[y][x]+1
                        q.append((ny, nx))
                pass
    return FAIL

    pass


if __name__ == "__main__":
    for _ in range(case := int(input())):
        c, r = map(int, input().split())
        maps = draw_maps(r)
        solution(c, r, maps)
    pass
