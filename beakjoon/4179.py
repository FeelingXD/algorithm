# 불
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
FIRE = 'F'
WALL = '#'
JIHUN = 'J'
PATH = '.'
FAIL = "IMPOSSIBLE"
MARK = '_'


def draw_maps(row):
    maps = []
    for _ in range(row):
        maps.append(list(input().strip()))
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
            if maps[y][x] == JIHUN:
                return (y, x)


def solution(c, r, maps):
    print(bfs(maps, r, c))
    pass


def bfs(maps, r, c):
    
    visited = [[0]*c for _ in range(r)]
    q = deque()
    
    # 지훈 추가
    jy, jx = find_str(maps)
    q.append((1, jy, jx))
    visited[jy][jx] = 1
    
    # 불
    for fire in find_fires(maps):
        y, x = fire
        q.append((-1, y, x))
        visited[y][x] = -1  # 불은 -1 표시
        
    while q:
        t, cy, cx = q.popleft()
        for dy, dx in moves:
            ny, nx = dy+cy, dx+cx
            # 맵탈출시 이전 visited 값 반환
            # t가 -1 인 경우 불
            if ((ny < 0 or ny >= len(maps)) or (nx < 0 or nx >= len(maps[0]))) and t > 0 and maps[cy][cx] != FIRE:
                return t
                pass
            else:
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if t < 0:  # 불
                        if maps[ny][nx] not in (WALL, FIRE):
                            maps[ny][nx] = FIRE
                            q.append((-1, ny, nx))
                    else:  # 사람
                        if maps[ny][nx] == PATH:
                            maps[ny][nx] = MARK  # 방문지역 마크처리
                            q.append((t+1, ny, nx))

    return FAIL
    pass


if __name__ == "__main__":
    r, c = map(int, input().split())
    maps = draw_maps(r)
    solution(c, r, maps)
    pass
