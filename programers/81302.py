# 거리두기 확인하기
from collections import deque
WALL = 'X'
PATH = 'O'
PERSON = 'P'
moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solution(places):
    answer = []
    for maps in places:
        able = True
        for y in range(len(maps)):
            for x in range(len(maps[0])):
                if maps[y][x] == PERSON:
                    if not bfs(x, y, maps):
                        able = False
                        continue
        answer.append(1) if able else answer.append(0)
    return answer


def bfs(x, y, maps):  # 사용자 기준으로 맨해튼 검사
    q = deque()
    q.append((y, x, 0))
    visited = [[False]*5 for _ in range(5)]
    visited[y][x] = True
    while q:
        cy, cx, d = q.popleft()
        for move in moves:
            dy, dx = move
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < 5 and 0 <= nx < 5 and maps[ny][nx] != WALL and not visited[ny][nx] and d < 2:
                if maps[ny][nx] != PERSON:  # 사람일 아닐경우만 큐에 추가하기
                    visited[ny][nx] = True
                    q.append((ny, nx, d+1))
                else:
                    return False
    return True
