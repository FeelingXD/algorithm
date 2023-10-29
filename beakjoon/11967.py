# 불켜기
from collections import defaultdict, deque
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(N, M):
    for _ in range(M):
        y, x, ly, lx = map(int, input().split())
        dic[(y, x)].append((ly, lx))
    print(bfs(N))
    pass


def bfs(N):

    q = deque()
    visited = [[False]*(N+1) for _ in range(N+1)]
    light = [[False]*(N+1) for _ in range(N+1)]
    light[1][1] = True
    visited[1][1] = True
    cnt = 1
    q.append((1, 1))
    while q:
        y, x = q.popleft()
        # 불켜기
        for py, px in dic[(y, x)]:
            if not light[py][px]:
                light[py][px] = True
                cnt += 1
                for dy, dx in moves:
                    ny = py+dy
                    nx = px+dx
                    if not (0 <= ny <= N and 0 <= nx <= N):
                        continue
                    if visited[ny][nx]:
                        q.append((ny, nx))
        # 움직이기
        for dy, dx in moves:
            ny = y+dy
            nx = x+dx
            if 0 <= ny <= N and 0 <= nx <= N:
                if not visited[ny][nx] and light[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return cnt
    pass


if __name__ == "__main__":
    global dic
    dic = defaultdict(list)
    N, M = map(int, input().split())
    solution(N, M)

    pass
