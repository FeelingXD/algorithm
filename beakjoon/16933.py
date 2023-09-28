# 벽부수고 이동하기 3
from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":

    N, M, K = map(int, input().split())

    board = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0, 1))  # (행,열, 벽을 부순횟수, 낮이자 시작거리)

    while q:
        x, y, z, ans = q.popleft()
        if x == N-1 and y == M-1:
            print(ans)
            exit()

        daytime = ans % 2
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:        # 다음위치가 벽이 아니고 첫방문이면
                    visited[nx][ny][z] = ans
                    q.append((nx, ny, z, ans+1))
                if board[nx][ny] == 1 and z < K and visited[nx][ny][z+1] == 0:
                    if daytime:
                        visited[nx][ny][z+1] = ans
                        q.append((nx, ny, z+1, ans+1))
                    else:
                        q.append((x, y, z, ans+1))

    print(-1)
