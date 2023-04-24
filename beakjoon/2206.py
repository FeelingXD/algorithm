# 벽부수고 이동하기
from collections import deque
n, m = map(int, input().split())
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[[0]*2 for i in range(m)] for j in range(n)]
visited[0][0][0] = 1


def bfs():
    q = deque()
    q.append((0, 0, 0))

    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for move in moves:
            nx = x+move[0]
            ny = y+move[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 엣지 graph 0이동가능 1벽
                continue
            if graph[nx][ny] == 1 and z == 0:  # 벽을 부술경우
                visited[nx][ny][1] = visited[x][y][0]+1
                q.append((nx, ny, 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append((nx, ny, z))
    return -1


print(bfs())
