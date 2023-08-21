# 토마토
import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())
visited = [[[False for _ in range(M)] for y in range(N)] for z in range(H)]

# for z in range(H):
#     for y in range(N):
#         print(visited[z][y])

board = []
for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int, input().split())))
    board.append(floor)


def find_tomato(board, visited):
    tomatoes = []  # xyz
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if board[z][y][x] == 1:
                    tomatoes.append([x, y, z, 0])
                    visited[z][y][x] = True
                elif board[z][y][x] == -1:
                    visited[z][y][x] = True
    return tomatoes


def check_visited(visited):
    for z in range(H):
        for y in range(N):
            if False in visited[z][y]:
                return True
    return False


def bfs(board, visited):
    preset_tomatoes = find_tomato(board, visited)
    q = deque(preset_tomatoes)
    answer = 0
    while q:
        x, y, z, depth = q.popleft()
        if depth > answer:
            answer = depth
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                q.append([nx, ny, nz, depth+1])
    if check_visited(visited):
        return -1
    return answer


print(bfs(board, visited))
