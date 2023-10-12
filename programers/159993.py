# 미로 탈출
from collections import deque
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
WALL = "X"
ROAD = "O"


def dfs(st, target, maps):
    # r,c = y x
    y, x = st  # 시작지점

    r = len(maps)
    c = len(maps[0])
    visited = [[False]*c for _ in range(r)]
    q = deque()
    visited[y][x] = 1
    q.append((y, x, 0))
    while q:
        y, x, d = q.popleft()
        if (y, x) == target:
            return d
        for move in moves:
            dy, dx = move
            ny, nx = y+dy, x+dx
            # 새로운 좌표가 벽이아니고 제한에 걸리지않을때
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] != WALL and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, d+1))
    return -1


def find_pos(maps):
    dic = {}
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S" or maps[y][x] == "E" or maps[y][x] == "L":  # 시작지점, 출구 ,레버 좌표
                dic[maps[y][x]] = (y, x)
    return dic


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    poses = find_pos(maps)
    answer = 0
    # 시작지점 부터 레버까지
    tmp = dfs(poses["S"], poses["L"], maps)
    if tmp == -1:
        return -1
    else:
        answer += tmp
    # 레버부터 출구까지
    tmp = dfs(poses["L"], poses["E"], maps)
    if tmp == -1:
        return -1
    else:
        answer += tmp

    return answer


print("🐍", solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
