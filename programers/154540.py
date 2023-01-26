# 무인도 여행
import sys
sys.setrecursionlimit(50000000)
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
score = 0


def solution(maps):
    global score
    answer = []
    visited = [[0]*len(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                visited[i][j] = 1

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if visited[i][j] == 1:
                dfs(maps, visited, i, j)
                answer.append(score)
                score = 0
    answer.sort()
    print(answer)
    return [-1] if answer == [] else answer


def dfs(maps, visited, x, y):
    global score
    visited[x][y] = 0
    score += int(maps[x][y])

    for d in dirs:
        nx = x+d[0]
        ny = y+d[1]

        if nx < 0 or len(maps) <= nx or ny < 0 or len(maps[0]) <= ny:
            continue

        if visited[nx][ny] == 1:
            dfs(maps, visited, nx, ny)


solution(["X591X", "X115X", "12321", "1XXX1"])
solution(["11XXX", "11XXX", "12311", "1XXX1"])
print(solution(["XXX1", "XX1X", "XX2X"]))
