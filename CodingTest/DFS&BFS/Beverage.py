# 음료수 얼려먹기
# n x m 크기의 얼음 틀이있다. 구멍이 둟려있는붑분은 0 칸막이가 존재하는부분은 1로표시
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우 롤 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음틀의 개수를 구하는 프로그램을 작성하시오

# 입력 1: 첫 벗째 줄에서 얼음 틀의 세로 길이 n 과 가로의 길이가 주어진다.

# DFS
import sys
graph = []
n, m = map(int, sys.stdin.readline().split())

for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
