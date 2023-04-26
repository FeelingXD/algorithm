# 1012 유기농배추
import sys
sys.setrecursionlimit(10**6)

case = int(input())
moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def dfs(graph, x, y):
    graph[y][x] = 2

    for move in moves:
        nx = x+move[0]
        ny = y+move[1]
        if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
            if graph[ny][nx] == 1:
                dfs(graph, nx, ny)


for _ in range(case):
    cnt = 0
    m, n, cabbages = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(cabbages):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(graph, x, y)
                cnt += 1

    print(cnt)
